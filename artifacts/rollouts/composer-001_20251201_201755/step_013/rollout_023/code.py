
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
    (0.0, 36, 100), # Kick on 1
    (0.375, 42, 100), # Hihat on &1
    (0.75, 38, 100), # Snare on 2
    (1.125, 42, 100), # Hihat on &2
    (1.5, 36, 100), # Kick on 3
    (1.875, 42, 100), # Hihat on &3
    (2.25, 38, 100), # Snare on 4
    (2.625, 42, 100), # Hihat on &4
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.1875))

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: F2 (root), Ab2 (fifth), Gb2 (chromatic approach), F2 (resolve)
bass_notes = [
    (1.5, 38, 100), # F2 (root)
    (1.75, 40, 100), # Gb2 (chromatic approach)
    (2.0, 39, 100), # Ab2 (fifth)
    (2.25, 38, 100), # F2 (resolve)
]
for time, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, D)
piano_notes = [
    (1.5, 65, 100), # F (F4)
    (1.5, 70, 100), # Ab (Ab4)
    (1.5, 72, 100), # C (C5)
    (1.5, 74, 100), # D (D5)
]
for time, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (1.5, 66, 100), # G (G4)
    (1.5, 69, 100), # Bb (Bb4)
    (2.0, 66, 100), # G (G4) - repeat
    (2.5, 69, 100), # Bb (Bb4) - resolve
]
for time, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: F2 (root), Ab2 (fifth), Gb2 (chromatic approach), F2 (resolve)
bass_notes = [
    (3.0, 38, 100), # F2 (root)
    (3.25, 40, 100), # Gb2 (chromatic approach)
    (3.5, 39, 100), # Ab2 (fifth)
    (3.75, 38, 100), # F2 (resolve)
]
for time, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Piano: Bbm7 (Bb, Db, F, G)
piano_notes = [
    (3.0, 69, 100), # Bb (Bb4)
    (3.0, 71, 100), # Db (Db5)
    (3.0, 72, 100), # F (F5)
    (3.0, 74, 100), # G (G5)
]
for time, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (3.0, 69, 100), # Bb (Bb4)
    (3.0, 72, 100), # F (F5)
    (3.5, 69, 100), # Bb (Bb4) - repeat
    (4.0, 72, 100), # F (F5) - resolve
]
for time, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: F2 (root), Ab2 (fifth), Gb2 (chromatic approach), F2 (resolve)
bass_notes = [
    (4.5, 38, 100), # F2 (root)
    (4.75, 40, 100), # Gb2 (chromatic approach)
    (5.0, 39, 100), # Ab2 (fifth)
    (5.25, 38, 100), # F2 (resolve)
]
for time, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Piano: Fm7 (F, Ab, C, D)
piano_notes = [
    (4.5, 65, 100), # F (F4)
    (4.5, 70, 100), # Ab (Ab4)
    (4.5, 72, 100), # C (C5)
    (4.5, 74, 100), # D (D5)
]
for time, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (4.5, 66, 100), # G (G4)
    (4.5, 69, 100), # Bb (Bb4)
    (5.0, 66, 100), # G (G4) - repeat
    (5.5, 69, 100), # Bb (Bb4) - resolve
]
for time, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Drums: Bar 3 and Bar 4
for bar in [3, 4]:
    start = bar * 1.5
    drum_notes = [
        (start, 36, 100), # Kick on 1
        (start + 0.375, 42, 100), # Hihat on &1
        (start + 0.75, 38, 100), # Snare on 2
        (start + 1.125, 42, 100), # Hihat on &2
        (start + 1.5, 36, 100), # Kick on 3
        (start + 1.875, 42, 100), # Hihat on &3
        (start + 2.25, 38, 100), # Snare on 4
        (start + 2.625, 42, 100), # Hihat on &4
    ]
    for time, note, velocity in drum_notes:
        drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.1875))

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
