
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(1):
    start = bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick3 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare2 = pretty_midi.Note(velocity=110, pitch=38, start=start + 0.375, end=start + 0.75)
    snare4 = pretty_midi.Note(velocity=110, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    for i in range(8):
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.125)
        drums.notes.append(hihat)
    drums.notes.extend([kick1, kick3, snare2, snare4])

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Bass line: walking line, chromatic approaches, no repeated notes
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=57, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=58, start=1.875, end=2.25), # Eb
    pretty_midi.Note(velocity=90, pitch=60, start=2.25, end=2.625), # F
    pretty_midi.Note(velocity=90, pitch=62, start=2.625, end=3.0),  # G
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=90, pitch=60, start=3.375, end=3.75), # F
    pretty_midi.Note(velocity=90, pitch=58, start=3.75, end=4.125), # Eb
    pretty_midi.Note(velocity=90, pitch=57, start=4.125, end=4.5),  # D
    pretty_midi.Note(velocity=90, pitch=57, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=90, pitch=58, start=4.875, end=5.25), # Eb
    pretty_midi.Note(velocity=90, pitch=60, start=5.25, end=5.625), # F
    pretty_midi.Note(velocity=90, pitch=62, start=5.625, end=6.0),  # G
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
# Bar 2: D7 (D, F#, A, C)
piano_notes = [
    pretty_midi.Note(velocity=95, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875),  # F#
    pretty_midi.Note(velocity=85, pitch=69, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=80, pitch=64, start=1.5, end=1.875),  # C
]
# Bar 3: G7 (G, B, D, F)
piano_notes.extend([
    pretty_midi.Note(velocity=95, pitch=67, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.375),  # B
    pretty_midi.Note(velocity=85, pitch=69, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=80, pitch=67, start=3.0, end=3.375),  # F
])
# Bar 4: C7 (C, E, G, B)
piano_notes.extend([
    pretty_midi.Note(velocity=95, pitch=64, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.875),  # E
    pretty_midi.Note(velocity=85, pitch=71, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=80, pitch=74, start=4.5, end=4.875),  # B
])
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D - F# - G - D (Dorian flavor)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.6875),  # D
    pretty_midi.Note(velocity=110, pitch=67, start=1.6875, end=1.875), # F#
    pretty_midi.Note(velocity=110, pitch=69, start=1.875, end=2.0625), # G
    pretty_midi.Note(velocity=110, pitch=62, start=2.0625, end=2.25),  # D
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.1875),  # D
    pretty_midi.Note(velocity=110, pitch=67, start=3.1875, end=3.375), # F#
    pretty_midi.Note(velocity=110, pitch=69, start=3.375, end=3.5625), # G
    pretty_midi.Note(velocity=110, pitch=62, start=3.5625, end=3.75),  # D
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.6875),  # D
    pretty_midi.Note(velocity=110, pitch=67, start=4.6875, end=4.875), # F#
    pretty_midi.Note(velocity=110, pitch=69, start=4.875, end=5.0625), # G
    pretty_midi.Note(velocity=110, pitch=62, start=5.0625, end=5.25),  # D
]
sax.notes.extend(sax_notes)

# Drums: Continue for bars 2-4
for bar in range(2, 4):
    start = bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick3 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare2 = pretty_midi.Note(velocity=110, pitch=38, start=start + 0.375, end=start + 0.75)
    snare4 = pretty_midi.Note(velocity=110, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    for i in range(8):
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.125)
        drums.notes.append(hihat)
    drums.notes.extend([kick1, kick3, snare2, snare4])

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
