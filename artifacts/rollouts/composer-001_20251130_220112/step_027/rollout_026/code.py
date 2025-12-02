
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
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Bass: Walking line, chromatic approaches, never the same note twice
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=43, start=1.5, end=1.875),  # Fm root
    pretty_midi.Note(velocity=80, pitch=44, start=1.875, end=2.25), # b9
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625), # 7
    pretty_midi.Note(velocity=80, pitch=41, start=2.625, end=3.0),  # b7
    pretty_midi.Note(velocity=80, pitch=40, start=3.0, end=3.375),  # Eb
    pretty_midi.Note(velocity=80, pitch=39, start=3.375, end=3.75), # D
    pretty_midi.Note(velocity=80, pitch=38, start=3.75, end=4.125), # C
    pretty_midi.Note(velocity=80, pitch=41, start=4.125, end=4.5),  # b7
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),  # 7
    pretty_midi.Note(velocity=80, pitch=44, start=4.875, end=5.25), # b9
    pretty_midi.Note(velocity=80, pitch=43, start=5.25, end=5.625), # root
    pretty_midi.Note(velocity=80, pitch=45, start=5.625, end=6.0),  # #9
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=60, start=1.5, end=1.875),  # Fm7 - F
    pretty_midi.Note(velocity=80, pitch=64, start=1.5, end=1.875),  # Fm7 - Ab
    pretty_midi.Note(velocity=80, pitch=67, start=1.5, end=1.875),  # Fm7 - C
    pretty_midi.Note(velocity=80, pitch=70, start=1.5, end=1.875),  # Fm7 - Eb
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=60, start=2.625, end=2.8125),  # Fm7 - F
    pretty_midi.Note(velocity=80, pitch=64, start=2.625, end=2.8125),  # Fm7 - Ab
    pretty_midi.Note(velocity=80, pitch=67, start=2.625, end=2.8125),  # Fm7 - C
    pretty_midi.Note(velocity=80, pitch=70, start=2.625, end=2.8125),  # Fm7 - Eb
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=60, start=4.125, end=4.3125),  # Fm7 - F
    pretty_midi.Note(velocity=80, pitch=64, start=4.125, end=4.3125),  # Fm7 - Ab
    pretty_midi.Note(velocity=80, pitch=67, start=4.125, end=4.3125),  # Fm7 - C
    pretty_midi.Note(velocity=80, pitch=70, start=4.125, end=4.3125),  # Fm7 - Eb
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Fm - Ab, Bb, C, Eb
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=64, start=1.5, end=1.6875),  # Ab
    pretty_midi.Note(velocity=110, pitch=62, start=1.6875, end=1.875), # Bb
    pretty_midi.Note(velocity=110, pitch=60, start=1.875, end=2.0625), # F
    pretty_midi.Note(velocity=110, pitch=67, start=2.0625, end=2.25),  # C
    pretty_midi.Note(velocity=110, pitch=64, start=2.25, end=2.4375),  # Ab
    pretty_midi.Note(velocity=110, pitch=62, start=2.4375, end=2.625), # Bb
    pretty_midi.Note(velocity=110, pitch=60, start=2.625, end=2.8125), # F
    pretty_midi.Note(velocity=110, pitch=67, start=2.8125, end=3.0),   # C
    pretty_midi.Note(velocity=110, pitch=64, start=3.0, end=3.1875),  # Ab
    pretty_midi.Note(velocity=110, pitch=62, start=3.1875, end=3.375), # Bb
    pretty_midi.Note(velocity=110, pitch=60, start=3.375, end=3.5625), # F
    pretty_midi.Note(velocity=110, pitch=67, start=3.5625, end=3.75),  # C
    pretty_midi.Note(velocity=110, pitch=64, start=3.75, end=3.9375),  # Ab
    pretty_midi.Note(velocity=110, pitch=62, start=3.9375, end=4.125), # Bb
    pretty_midi.Note(velocity=110, pitch=60, start=4.125, end=4.3125), # F
    pretty_midi.Note(velocity=110, pitch=67, start=4.3125, end=4.5),   # C
    pretty_midi.Note(velocity=110, pitch=64, start=4.5, end=4.6875),  # Ab
    pretty_midi.Note(velocity=110, pitch=62, start=4.6875, end=4.875), # Bb
    pretty_midi.Note(velocity=110, pitch=60, start=4.875, end=5.0625), # F
    pretty_midi.Note(velocity=110, pitch=67, start=5.0625, end=5.25),  # C
    pretty_midi.Note(velocity=110, pitch=64, start=5.25, end=5.4375),  # Ab
    pretty_midi.Note(velocity=110, pitch=62, start=5.4375, end=5.625), # Bb
    pretty_midi.Note(velocity=110, pitch=60, start=5.625, end=5.8125), # F
    pretty_midi.Note(velocity=110, pitch=67, start=5.8125, end=6.0),   # C
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375)
    kick3 = pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 1.125, end=bar_start + 1.5)
    # Snare on 2 and 4
    snare2 = pretty_midi.Note(velocity=110, pitch=38, start=bar_start + 0.75, end=bar_start + 0.875)
    snare4 = pretty_midi.Note(velocity=110, pitch=38, start=bar_start + 1.875, end=bar_start + 2.0)
    # Hi-hat on every eighth
    for i in range(0, 8):
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=bar_start + i*0.1875, end=bar_start + (i+1)*0.1875)
        drums.notes.append(hihat)
    # Add kicks and snares
    drums.notes.extend([kick1, kick3, snare2, snare4])

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
