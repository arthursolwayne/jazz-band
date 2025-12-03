
import pretty_midi

# Create a new MIDI file with tempo 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Instruments for the quartet
sax = pretty_midi.Instrument(program=66)       # Tenor sax (Dante)
bass = pretty_midi.Instrument(program=33)      # Double bass (Marcus)
piano = pretty_midi.Instrument(program=0)      # Piano (Diane)
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums (Little Ray)

# Drum notes: kick=36, snare=38, hihat=42
drum_notes = {
    'kick': 36,
    'snare': 38,
    'hihat': 42
}

# Time per bar (1.5 seconds at 160 BPM)
bar_length = 1.5

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(1):
    start_time = bar * bar_length
    # Kick on beat 1 and 3
    kick_times = [start_time + 0.0, start_time + 0.75]
    for t in kick_times:
        note = pretty_midi.Note(velocity=80, pitch=drum_notes['kick'], start=t, end=t + 0.1)
        drums.notes.append(note)
    # Snare on beat 2 and 4
    snare_times = [start_time + 0.375, start_time + 1.125]
    for t in snare_times:
        note = pretty_midi.Note(velocity=100, pitch=drum_notes['snare'], start=t, end=t + 0.1)
        drums.notes.append(note)
    # Hihat on every eighth note
    for t in [start_time + 0.0, start_time + 0.375, start_time + 0.75, start_time + 1.125]:
        note = pretty_midi.Note(velocity=70, pitch=drum_notes['hihat'], start=t, end=t + 0.1)
        drums.notes.append(note)

# Bar 2: Introduce the full quartet (1.5 - 3.0s)
# Bass: Walking line (F2 to C3, MIDI 53 to 60), roots and fifths with chromatic approaches
# Chord: F7 (F, A, C, E♭)
# Bass line: F → E♭ → C → B♭ (chromatic approach to C)
bass_notes = [
    (1.5, 53),   # F2
    (1.875, 50), # E♭2
    (2.25, 57),  # C3
    (2.625, 60)  # B♭3 (approach to C)
]
for t, pitch in bass_notes:
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=t, end=t + 0.375)
    bass.notes.append(note)

# Piano: Open voicings, F7 on bar 2 (F, A, C, E♭), then Gm7 on bar 3, then C7 on bar 4
# Comp on 2 and 4
# Bar 2: F7
piano_notes = [
    (1.5, 53), (1.5, 65), (1.5, 60), (1.5, 62)  # F, A, C, E♭
]
for t, pitch in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=t, end=t + 0.375)
    piano.notes.append(note)

# Bar 3: Gm7 (G, B♭, D, F)
# Comp on 2 and 4
piano_notes = [
    (3.0, 67), (3.0, 62), (3.0, 64), (3.0, 53)  # G, B♭, D, F
]
for t, pitch in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=t, end=t + 0.375)
    piano.notes.append(note)

# Bar 4: C7 (C, E, G, B♭)
# Comp on 2 and 4
piano_notes = [
    (4.5, 60), (4.5, 64), (4.5, 67), (4.5, 62)  # C, E, G, B♭
]
for t, pitch in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=t, end=t + 0.375)
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging, come back and finish it.
# Melody: F (1.5s), A (1.875s), C (2.25s), F (2.625s) then rest until 3.0s
# Then return with a half-step resolution: F (3.0s), E♭ (3.375s)
sax_notes = [
    (1.5, 53),  # F2
    (1.875, 58),  # A2
    (2.25, 60),  # C3
    (2.625, 53),  # F2
    (3.0, 53),  # F2
    (3.375, 50)  # E♭2
]
for t, pitch in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=t, end=t + 0.375)
    sax.notes.append(note)

# Create the final MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save as a MIDI file
# midi.write disabled
