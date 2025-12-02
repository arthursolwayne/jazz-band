
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
    (0.0, 36, 100),  # Kick on 1
    (0.75, 42, 100), # Hihat on &1
    (1.0, 38, 100),  # Snare on 2
    (1.25, 42, 100), # Hihat on &2
    (1.5, 36, 100),  # Kick on 3
    (1.75, 42, 100), # Hihat on &3
    (2.0, 38, 100),  # Snare on 4
    (2.25, 42, 100), # Hihat on &4
]
for start, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, start, start + 0.25))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): F2, Ab2, Bb2, Db3, etc. Walking line with chromatic approaches
bass_notes = [
    (1.5, 72, 100),  # F2
    (2.0, 70, 100),  # Eb2 (chromatic approach)
    (2.5, 69, 100),  # D2 (chromatic approach)
    (3.0, 71, 100),  # E2 (root)
    (3.5, 69, 100),  # D2 (chromatic approach)
    (4.0, 67, 100),  # C2 (chromatic approach)
    (4.5, 68, 100),  # C#2 (chromatic approach)
    (5.0, 72, 100),  # F2
    (5.5, 70, 100),  # Eb2
]
for start, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, start, start + 0.5))

# Piano (Diane): Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, D)
piano_notes = [
    (1.5, 78, 100),  # F4
    (1.5, 81, 100),  # Ab4
    (1.5, 72, 100),  # C4
    (1.5, 74, 100),  # D4
]
# Bar 3: Bb7 (Bb, D, F, Ab)
piano_notes.extend([
    (2.5, 73, 100),  # Bb4
    (2.5, 77, 100),  # D4
    (2.5, 78, 100),  # F4
    (2.5, 81, 100),  # Ab4
])
# Bar 4: Cm7 (C, Eb, G, Bb)
piano_notes.extend([
    (3.5, 72, 100),  # C4
    (3.5, 69, 100),  # Eb4
    (3.5, 76, 100),  # G4
    (3.5, 73, 100),  # Bb4
])
for start, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, start, start + 0.5))

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 2 (1.5 - 3.0s)
drum_notes = [
    (1.5, 36, 100),  # Kick 1
    (1.75, 42, 100), # Hihat &1
    (2.0, 38, 100),  # Snare 2
    (2.25, 42, 100), # Hihat &2
    (2.5, 36, 100),  # Kick 3
    (2.75, 42, 100), # Hihat &3
    (3.0, 38, 100),  # Snare 4
    (3.25, 42, 100), # Hihat &4
]
for start, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, start, start + 0.25))

# Bar 3 (3.0 - 4.5s)
drum_notes = [
    (3.0, 36, 100),  # Kick 1
    (3.25, 42, 100), # Hihat &1
    (3.5, 38, 100),  # Snare 2
    (3.75, 42, 100), # Hihat &2
    (4.0, 36, 100),  # Kick 3
    (4.25, 42, 100), # Hihat &3
    (4.5, 38, 100),  # Snare 4
    (4.75, 42, 100), # Hihat &4
]
for start, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, start, start + 0.25))

# Bar 4 (4.5 - 6.0s)
drum_notes = [
    (4.5, 36, 100),  # Kick 1
    (4.75, 42, 100), # Hihat &1
    (5.0, 38, 100),  # Snare 2
    (5.25, 42, 100), # Hihat &2
    (5.5, 36, 100),  # Kick 3
    (5.75, 42, 100), # Hihat &3
    (6.0, 38, 100),  # Snare 4
    (6.25, 42, 100), # Hihat &4
]
for start, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, start, start + 0.25))

# Saxophone (Dante): One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F4, Ab4, Bb4, F4 (melodic fragment, not scale runs)
sax_notes = [
    (1.5, 78, 100),  # F4
    (1.75, 81, 100), # Ab4
    (2.0, 77, 100),  # Bb4
    (2.5, 78, 100),  # F4 (delayed resolution)
    (3.5, 78, 100),  # F4 (return)
    (3.75, 81, 100), # Ab4
    (4.0, 77, 100),  # Bb4
    (4.5, 78, 100),  # F4
]
for start, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, start, start + 0.25))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
