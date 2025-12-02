
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_kick = pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375)
drum_snare = pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125)
drum_hihat = pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5)
drums.notes.extend([drum_kick, drum_snare, drum_hihat])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, no repeated notes
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=45, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=46, start=1.875, end=2.25), # G
    pretty_midi.Note(velocity=90, pitch=44, start=2.25, end=2.625), # E
    pretty_midi.Note(velocity=90, pitch=43, start=2.625, end=3.0),  # D
    pretty_midi.Note(velocity=90, pitch=47, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=90, pitch=48, start=3.375, end=3.75), # Bb
    pretty_midi.Note(velocity=90, pitch=46, start=3.75, end=4.125), # G
    pretty_midi.Note(velocity=90, pitch=45, start=4.125, end=4.5),  # F
    pretty_midi.Note(velocity=90, pitch=47, start=4.5, end=4.875),  # A
    pretty_midi.Note(velocity=90, pitch=48, start=4.875, end=5.25), # Bb
    pretty_midi.Note(velocity=90, pitch=46, start=5.25, end=5.625), # G
    pretty_midi.Note(velocity=90, pitch=45, start=5.625, end=6.0),  # F
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=45, start=1.5, end=2.25),  # F7: F, A, C, Eb
    pretty_midi.Note(velocity=90, pitch=50, start=1.5, end=2.25),
    pretty_midi.Note(velocity=90, pitch=48, start=1.5, end=2.25),
    pretty_midi.Note(velocity=90, pitch=52, start=1.5, end=2.25),
    pretty_midi.Note(velocity=90, pitch=45, start=3.0, end=3.75),
    pretty_midi.Note(velocity=90, pitch=50, start=3.0, end=3.75),
    pretty_midi.Note(velocity=90, pitch=48, start=3.0, end=3.75),
    pretty_midi.Note(velocity=90, pitch=52, start=3.0, end=3.75),
    pretty_midi.Note(velocity=90, pitch=45, start=4.5, end=5.25),
    pretty_midi.Note(velocity=90, pitch=50, start=4.5, end=5.25),
    pretty_midi.Note(velocity=90, pitch=48, start=4.5, end=5.25),
    pretty_midi.Note(velocity=90, pitch=52, start=4.5, end=5.25),
]
piano.notes.extend(piano_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = bar * 1.5
    drum_kick = pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375)
    drum_snare = pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.75, end=bar_start + 1.125)
    drum_hihat = pretty_midi.Note(velocity=80, pitch=42, start=bar_start, end=bar_start + 1.5)
    drums.notes.extend([drum_kick, drum_snare, drum_hihat])

# Sax: Motif in F, short and singable
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=2.625),  # E
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0),   # F
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=100, pitch=60, start=3.375, end=3.75), # E
    pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.5),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=100, pitch=60, start=4.875, end=5.25), # E
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.625), # F
    pretty_midi.Note(velocity=100, pitch=64, start=5.625, end=6.0),  # G
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
