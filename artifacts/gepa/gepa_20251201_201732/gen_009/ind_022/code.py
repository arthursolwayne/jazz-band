
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
    # Bar 1: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line (F2, G2, Ab2, A2, Bb2, B2, C2, Db2)
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=80, pitch=53, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=80, pitch=55, start=1.875, end=2.25), # G2
    pretty_midi.Note(velocity=80, pitch=54, start=2.25, end=2.625), # Ab2
    pretty_midi.Note(velocity=80, pitch=56, start=2.625, end=3.0),  # A2

    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=80, pitch=57, start=3.0, end=3.375),  # Bb2
    pretty_midi.Note(velocity=80, pitch=59, start=3.375, end=3.75), # B2
    pretty_midi.Note(velocity=80, pitch=60, start=3.75, end=4.125), # C2
    pretty_midi.Note(velocity=80, pitch=58, start=4.125, end=4.5),  # Db2

    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=80, pitch=53, start=4.5, end=4.875),  # F2
    pretty_midi.Note(velocity=80, pitch=55, start=4.875, end=5.25), # G2
    pretty_midi.Note(velocity=80, pitch=54, start=5.25, end=5.625), # Ab2
    pretty_midi.Note(velocity=80, pitch=56, start=5.625, end=6.0),  # A2
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, Eb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.5 + 0.375),  # F (C4)
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.5 + 0.375),  # Eb (E3)
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.5 + 0.375),  # G (G3)
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.5 + 0.375),  # Ab (Ab3)

    # Bar 3: Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=100, pitch=70, start=3.0, end=3.0 + 0.375),  # Bb (Bb4)
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.0 + 0.375),  # D (D4)
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.0 + 0.375),  # F (F4)
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.0 + 0.375),  # Ab (Ab4)

    # Bar 4: Cm7 (C, Eb, G, Bb)
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.5 + 0.375),  # C (C5)
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.5 + 0.375),  # Eb (Eb4)
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.5 + 0.375),  # G (G4)
    pretty_midi.Note(velocity=100, pitch=70, start=4.5, end=4.5 + 0.375),  # Bb (Bb4)
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F, Ab, Bb, F (Fm scale), with space on the third beat
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # F (F4)
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.25),  # Ab (Ab4)
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # Bb (Bb4)
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # F (F4)
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.75),  # Ab (Ab4)
    pretty_midi.Note(velocity=100, pitch=71, start=4.125, end=4.5),  # F (F4)
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # Bb (Bb4)
    pretty_midi.Note(velocity=100, pitch=71, start=5.25, end=5.625),  # F (F4)
]

for note in sax_notes:
    sax.notes.append(note)

# Drums: Bars 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    for i in range(4):
        pretty_midi.Note(velocity=100, pitch=42, start=start + i * 0.375, end=start + (i + 1) * 0.375)

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("wayne_intro.mid")
