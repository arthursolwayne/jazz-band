
import pretty_midi

# Create the MIDI file with 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Instruments
sax = pretty_midi.Instrument(program=66)       # Tenor sax
bass = pretty_midi.Instrument(program=33)      # Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drum notes: kick=36, snare=38, hihat=42
kick = 36
snare = 38
hihat = 42

# Bar 1: Drums only (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in [0]:
    for beat in [0, 2]:  # Kick on 1 and 3
        time = 1.5 * bar + beat * 0.375
        note = pretty_midi.Note(velocity=100, pitch=kick, start=time, end=time + 0.1)
        drums.notes.append(note)
    for beat in [1, 3]:  # Snare on 2 and 4
        time = 1.5 * bar + beat * 0.375
        note = pretty_midi.Note(velocity=100, pitch=snare, start=time, end=time + 0.1)
        drums.notes.append(note)
    for beat in range(0, 4):  # Hihat on every eighth
        time = 1.5 * bar + beat * 0.375
        note = pretty_midi.Note(velocity=90, pitch=hihat, start=time, end=time + 0.1)
        drums.notes.append(note)

# Bar 2-4: Full quartet (1.5 - 6.0s)
for bar in [1, 2, 3]:
    # Bass: walking line in Dm, chromatic approach to each chord
    # Dm7: D F A C
    # Chromatic approaches: C# to D, E to F, G to A, B to C
    # Bass line: C# D F E A G B C
    # Translated to bar 2: C# (beat 1), D (2), F (3), E (4)
    # Bar 3: A (1), G (2), B (3), C (4)
    # Bar 4: D (1), F (2), A (3), G (4) [chromatic to resolve back to D]

    # Determine bass notes
    if bar == 1:
        bass_notes = [1, 2, 5, 4]  # C#, D, F, E
    elif bar == 2:
        bass_notes = [6, 5, 8, 7]  # A, G, B, C
    elif bar == 3:
        bass_notes = [2, 5, 6, 5]  # D, F, A, G

    # Convert to MIDI pitch (C = 60, D = 62, etc.)
    # D = 62, F = 65, A = 69, C = 60
    # C# = 61, E = 64, G = 67, B = 71
    for beat, note in enumerate(bass_notes):
        time = 1.5 * bar + beat * 0.375
        # Map note to pitch
        if note == 1: pitch = 61  # C#
        elif note == 2: pitch = 62  # D
        elif note == 4: pitch = 64  # E
        elif note == 5: pitch = 65  # F
        elif note == 6: pitch = 67  # G
        elif note == 7: pitch = 69  # A
        elif note == 8: pitch = 71  # B
        note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.25)
        bass.notes.append(note)

    # Piano: 7th chords on 2 and 4
    # Dm7: D F A C
    # Chord on beat 2 and 4, root position
    for beat in [1, 3]:  # Beats 2 and 4
        time = 1.5 * bar + beat * 0.375
        # Dm7: D=62, F=65, A=69, C=60
        notes = [62, 65, 69, 60]
        for pitch in notes:
            note = pretty_midi.Note(velocity=90, pitch=pitch, start=time, end=time + 0.5)
            piano.notes.append(note)

    # Sax: Melody — 4-bar motif, starting on bar 2
    if bar == 1:
        # Bar 1: No sax
        continue
    elif bar == 2:
        # Start the motif
        # Dm7: D F A C
        # Motif: D (62), F (65), Bb (66), C (60)
        notes = [62, 65, 66, 60]
        for beat, pitch in enumerate(notes):
            time = 1.5 * bar + beat * 0.375
            note = pretty_midi.Note(velocity=110, pitch=pitch, start=time, end=time + 0.25)
            sax.notes.append(note)
    elif bar == 3:
        # Repeat the first two notes of the motif
        notes = [62, 65]
        for beat, pitch in enumerate(notes):
            time = 1.5 * bar + beat * 0.375
            note = pretty_midi.Note(velocity=110, pitch=pitch, start=time, end=time + 0.25)
            sax.notes.append(note)
    elif bar == 4:
        # Finish the motif: Bb (66), C (60)
        notes = [66, 60]
        for beat, pitch in enumerate(notes):
            time = 1.5 * bar + beat * 0.375
            note = pretty_midi.Note(velocity=110, pitch=pitch, start=time, end=time + 0.25)
            sax.notes.append(note)

    # Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
    for beat in [0, 2]:  # Kick on 1 and 3
        time = 1.5 * bar + beat * 0.375
        note = pretty_midi.Note(velocity=100, pitch=kick, start=time, end=time + 0.1)
        drums.notes.append(note)
    for beat in [1, 3]:  # Snare on 2 and 4
        time = 1.5 * bar + beat * 0.375
        note = pretty_midi.Note(velocity=100, pitch=snare, start=time, end=time + 0.1)
        drums.notes.append(note)
    for beat in range(0, 4):  # Hihat on every eighth
        time = 1.5 * bar + beat * 0.375
        note = pretty_midi.Note(velocity=90, pitch=hihat, start=time, end=time + 0.1)
        drums.notes.append(note)

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("jazz_intro.mid")
