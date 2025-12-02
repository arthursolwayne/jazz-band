
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=80, pitch=40, start=1.875, end=2.25),  # F2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=43, start=2.25, end=2.625),  # A2
    pretty_midi.Note(velocity=80, pitch=38, start=2.625, end=3.0),  # D2
    # Bar 3
    pretty_midi.Note(velocity=80, pitch=40, start=3.0, end=3.375),  # F2
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),  # G2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=43, start=3.75, end=4.125),  # A2
    pretty_midi.Note(velocity=80, pitch=38, start=4.125, end=4.5),  # D2
    # Bar 4
    pretty_midi.Note(velocity=80, pitch=40, start=4.5, end=4.875),  # F2
    pretty_midi.Note(velocity=80, pitch=41, start=4.875, end=5.25),  # F#2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=43, start=5.25, end=5.625),  # A2
    pretty_midi.Note(velocity=80, pitch=38, start=5.625, end=6.0),  # D2
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dmaj7 (D, F#, A, C#)
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=50, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=80, pitch=53, start=1.5, end=1.875),  # F#4
    pretty_midi.Note(velocity=80, pitch=55, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=80, pitch=58, start=1.5, end=1.875),  # C#5

    # Bar 3: G7 (G, B, D, F)
    pretty_midi.Note(velocity=80, pitch=55, start=3.0, end=3.375),  # G4
    pretty_midi.Note(velocity=80, pitch=57, start=3.0, end=3.375),  # B4
    pretty_midi.Note(velocity=80, pitch=59, start=3.0, end=3.375),  # D5
    pretty_midi.Note(velocity=80, pitch=61, start=3.0, end=3.375),  # F5

    # Bar 4: Cm7 (C, Eb, G, Bb)
    pretty_midi.Note(velocity=80, pitch=60, start=4.5, end=4.875),  # C5
    pretty_midi.Note(velocity=80, pitch=63, start=4.5, end=4.875),  # Eb5
    pretty_midi.Note(velocity=80, pitch=67, start=4.5, end=4.875),  # G5
    pretty_midi.Note(velocity=80, pitch=69, start=4.5, end=4.875),  # Bb5
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D4 - F#4 - A4 - D5 (D to D)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=2.25),  # F#4
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # A4
    pretty_midi.Note(velocity=100, pitch=71, start=2.625, end=3.0),  # D5
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # A4
    pretty_midi.Note(velocity=100, pitch=65, start=3.375, end=3.75),  # F#4
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.125),  # D4
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875),  # D5
]
for note in sax_notes:
    sax.notes.append(note)

# Drums: Bar 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 4):
    start_time = bar * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=start_time, end=start_time + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=start_time + 1.125, end=start_time + 1.5)
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=start_time + 0.75, end=start_time + 0.875)
    pretty_midi.Note(velocity=100, pitch=38, start=start_time + 1.875, end=start_time + 2.0)
    # Hihat on every eighth
    for i in range(4):
        pretty_midi.Note(velocity=80, pitch=42, start=start_time + i * 0.375, end=start_time + i * 0.375 + 0.375)

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
