
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.
drum_kick = pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375)
drums.notes.append(drum_kick)
drum_kick = pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5)
drums.notes.append(drum_kick)

drum_snare = pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125)
drums.notes.append(drum_snare)

drum_hihat = pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5)
drum_hihat = pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75)
drum_hihat = pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125)
drum_hihat = pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5)
drums.notes.append(drum_hihat)
drums.notes.append(drum_hihat)
drums.notes.append(drum_hihat)
drums.notes.append(drum_hihat)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line in Fm, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=63, start=1.875, end=2.25), # Eb
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.625), # D
    pretty_midi.Note(velocity=90, pitch=60, start=2.625, end=3.0),  # C
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=90, pitch=65, start=3.375, end=3.75), # Gb
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.125), # Ab
    pretty_midi.Note(velocity=90, pitch=64, start=4.125, end=4.5),  # F
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=90, pitch=60, start=4.875, end=5.25), # C
    pretty_midi.Note(velocity=90, pitch=64, start=5.25, end=5.625), # F
    pretty_midi.Note(velocity=90, pitch=63, start=5.625, end=6.0),  # Eb
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=64, start=1.875, end=2.25),  # F7
    pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=69, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=71, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=64, start=3.375, end=3.75),  # F7
    pretty_midi.Note(velocity=90, pitch=67, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=69, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=71, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=64, start=4.875, end=5.25),  # F7
    pretty_midi.Note(velocity=90, pitch=67, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=69, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=71, start=4.875, end=5.25),
]
piano.notes.extend(piano_notes)

# Drums: Bars 2-4
for bar in range(2, 5):
    bar_start = bar * 1.5
    drum_kick = pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375)
    drums.notes.append(drum_kick)
    drum_kick = pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 1.125, end=bar_start + 1.5)
    drums.notes.append(drum_kick)
    drum_snare = pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.75, end=bar_start + 1.125)
    drums.notes.append(drum_snare)
    for i in range(4):
        drum_hihat = pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 0.375 * i, end=bar_start + 0.375 * (i + 1))
        drums.notes.append(drum_hihat)

# Sax: Motif in Fm
# Start at bar 2 (1.5s), play a short motif, leave it hanging, then return to finish it
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=1.625, end=1.75),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=60, start=1.875, end=2.0),  # C
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.375),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=2.375, end=2.5),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=2.5, end=2.625),  # F
    pretty_midi.Note(velocity=100, pitch=60, start=2.625, end=2.75),  # C
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.125),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=3.125, end=3.25),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=3.25, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=60, start=3.375, end=3.5),  # C
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=3.875),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=3.875, end=4.0),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=4.0, end=4.125),  # F
    pretty_midi.Note(velocity=100, pitch=60, start=4.125, end=4.25),  # C
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.625),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=4.625, end=4.75),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=4.75, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=60, start=4.875, end=5.0),  # C
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.375),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=5.375, end=5.5),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=5.5, end=5.625),  # F
    pretty_midi.Note(velocity=100, pitch=60, start=5.625, end=5.75),  # C
    pretty_midi.Note(velocity=100, pitch=64, start=5.75, end=6.0),  # F
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_russo_intro.mid")
