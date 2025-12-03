
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
    # Bar 1
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5),     # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line - F2, G2, A2, C3 (MIDI 38, 43, 45, 52), with chromatic approach
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # F2 on 1
    pretty_midi.Note(velocity=100, pitch=39, start=1.875, end=2.25), # chromatic approach to G2
    pretty_midi.Note(velocity=100, pitch=43, start=2.25, end=2.625), # G2 on 2
    pretty_midi.Note(velocity=100, pitch=45, start=2.625, end=3.0),  # A2 on 3
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=100, pitch=63, start=1.5, end=1.75),  # A
    pretty_midi.Note(velocity=100, pitch=57, start=1.5, end=1.75),  # C
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.75),  # E
]

# Bar 3: Bb7 (Bb, D, F, Ab)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=50, start=3.0, end=3.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=58, start=3.0, end=3.25),  # D
    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=100, pitch=55, start=3.0, end=3.25),  # Ab
])

# Bar 4: C7 (C, E, G, Bb)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=57, start=4.5, end=4.75),  # C
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.75),  # E
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.75),  # G
    pretty_midi.Note(velocity=100, pitch=55, start=4.5, end=4.75),  # Bb
])

for note in piano_notes:
    piano.notes.append(note)

# Sax: Melody - short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F - G - Bb - F (MIDI 53, 55, 58, 53)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875),  # F on 1
    pretty_midi.Note(velocity=100, pitch=55, start=1.875, end=2.25), # G on 2
    pretty_midi.Note(velocity=100, pitch=58, start=2.25, end=2.625), # Bb on 3
    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=3.375),  # F on 4
]

# Fill in the rest of the motif with space and tension
sax_notes.append(pretty_midi.Note(velocity=100, pitch=53, start=4.5, end=4.875))  # Return to F on 1 of next bar

for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Drums (3.0 - 4.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=4.5),     # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 4: Drums (4.5 - 6.0s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=6.0),     # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line - Bb2, C2, D2, F2 (MIDI 50, 52, 53, 55), with chromatic approach
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=50, start=3.0, end=3.375),  # Bb2 on 1
    pretty_midi.Note(velocity=100, pitch=51, start=3.375, end=3.75), # chromatic approach to C2
    pretty_midi.Note(velocity=100, pitch=52, start=3.75, end=4.125), # C2 on 2
    pretty_midi.Note(velocity=100, pitch=53, start=4.125, end=4.5),  # D2 on 3
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 3: Bb7 (Bb, D, F, Ab)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=50, start=3.0, end=3.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=58, start=3.0, end=3.25),  # D
    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=100, pitch=55, start=3.0, end=3.25),  # Ab
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Continue the melody, resolve on F
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=58, start=3.0, end=3.375),  # Bb on 1
    pretty_midi.Note(velocity=100, pitch=53, start=3.375, end=3.75), # F on 2
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line - C2, D2, F2, G2 (MIDI 52, 53, 55, 57), with chromatic approach
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=52, start=4.5, end=4.875),  # C2 on 1
    pretty_midi.Note(velocity=100, pitch=53, start=4.875, end=5.25), # chromatic approach to D2
    pretty_midi.Note(velocity=100, pitch=53, start=5.25, end=5.625), # D2 on 2
    pretty_midi.Note(velocity=100, pitch=55, start=5.625, end=6.0),  # F2 on 3
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 4: C7 (C, E, G, Bb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=57, start=4.5, end=4.75),  # C
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.75),  # E
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.75),  # G
    pretty_midi.Note(velocity=100, pitch=55, start=4.5, end=4.75),  # Bb
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Complete the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=4.5, end=4.875),  # F on 1
    pretty_midi.Note(velocity=100, pitch=55, start=4.875, end=5.25), # G on 2
    pretty_midi.Note(velocity=100, pitch=58, start=5.25, end=5.625), # Bb on 3
    pretty_midi.Note(velocity=100, pitch=53, start=5.625, end=6.0),  # F on 4
]

for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
