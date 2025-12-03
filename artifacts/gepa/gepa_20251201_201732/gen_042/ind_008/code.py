
import pretty_midi

# Create a new MIDI file with tempo 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Initialize instruments
sax = pretty_midi.Instrument(program=66)       # Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Double Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Define MIDI note values
# Drums: kick=36, snare=38, hihat=42
# Bass: D2=38, G2=43
# Piano: Open voicings, varying chords
# Sax: Motif in F minor (F, Ab, Bb, C) with space and tension

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

# Bar 1: 0.0 - 1.5s
drum_notes = [
    (36, 0.0),  # Kick on beat 1
    (38, 0.5),  # Snare on beat 2
    (36, 1.0),  # Kick on beat 3
    (38, 1.5),  # Snare on beat 4
]
for note, time in drum_notes:
    note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25)
    drums.notes.append(note)

# Add hihat on every eighth note
for i in range(0, 6, 0.5):  # 6 beats at 160 BPM, 0.5s per eighth
    note = pretty_midi.Note(velocity=60, pitch=42, start=i, end=i + 0.125)
    drums.notes.append(note)

# Bar 2: 1.5 - 3.0s
# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
# Piano: Open voicings, different chord each bar, resolve on the last
# Sax: Motif starts here (F, Ab, Bb, C) — one short motif, make it sing
# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

# Bass: Root (D2, 38), then chromatic approach on 3rd beat (Eb, 40)
bass_notes = [
    (38, 1.5),  # D2 on beat 1
    (40, 2.0),  # Eb on beat 2 (chromatic approach)
    (43, 2.5),  # G2 on beat 3
    (38, 3.0),  # D2 on beat 4
]
for note, time in bass_notes:
    note = pretty_midi.Note(velocity=70, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(note)

# Piano: F7 (F, A, C, E) — open voicing
piano_notes = [
    (71, 1.5),  # F7 (F, A, C, E) — F (71), A (74), C (72), E (76)
    (74, 1.5),  # A
    (72, 1.5),  # C
    (76, 1.5),  # E
]
for note, time in piano_notes:
    note = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.5)
    piano.notes.append(note)

# Sax: Motif starting (F, Ab, Bb, C)
sax_notes = [
    (84, 1.5),  # F (84)
    (81, 2.0),  # Ab (81)
    (80, 2.5),  # Bb (80)
    (87, 3.0),  # C (87)
]
for note, time in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    sax.notes.append(note)

# Bar 3: 3.0 - 4.5s
# Bass: Root (D2, 38), then chromatic approach on 3rd beat (Eb, 40)
bass_notes = [
    (38, 3.0),  # D2 on beat 1
    (40, 3.5),  # Eb on beat 2 (chromatic approach)
    (43, 4.0),  # G2 on beat 3
    (38, 4.5),  # D2 on beat 4
]
for note, time in bass_notes:
    note = pretty_midi.Note(velocity=70, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(note)

# Piano: Bb7 (Bb, D, F, Ab) — open voicing
piano_notes = [
    (78, 3.0),  # Bb (78)
    (82, 3.0),  # D (82)
    (76, 3.0),  # F (76)
    (81, 3.0),  # Ab (81)
]
for note, time in piano_notes:
    note = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.5)
    piano.notes.append(note)

# Sax: Continue motif, leave it hanging (return to F on the 4th beat)
sax_notes = [
    (83, 3.0),  # F (83)
    (80, 3.5),  # Bb (80)
    (87, 4.0),  # C (87)
    (84, 4.5),  # F (84)
]
for note, time in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    sax.notes.append(note)

# Bar 4: 4.5 - 6.0s
# Bass: Root (D2, 38), then chromatic approach on 3rd beat (Eb, 40)
bass_notes = [
    (38, 4.5),  # D2 on beat 1
    (40, 5.0),  # Eb on beat 2 (chromatic approach)
    (43, 5.5),  # G2 on beat 3
    (38, 6.0),  # D2 on beat 4
]
for note, time in bass_notes:
    note = pretty_midi.Note(velocity=70, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(note)

# Piano: F7 (F, A, C, E) — open voicing
piano_notes = [
    (71, 4.5),  # F (71)
    (74, 4.5),  # A (74)
    (72, 4.5),  # C (72)
    (76, 4.5),  # E (76)
]
for note, time in piano_notes:
    note = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.5)
    piano.notes.append(note)

# Sax: Finish the motif with a return to F, leave it hanging
sax_notes = [
    (84, 4.5),  # F (84)
    (81, 5.0),  # Ab (81)
    (80, 5.5),  # Bb (80)
    (87, 6.0),  # C (87)
]
for note, time in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    sax.notes.append(note)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 4.5),  # Kick on beat 1
    (38, 5.0),  # Snare on beat 2
    (36, 5.5),  # Kick on beat 3
    (38, 6.0),  # Snare on beat 4
]
for note, time in drum_notes:
    note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25)
    drums.notes.append(note)

# Add hihat on every eighth note
for i in range(4.5, 6.0, 0.5):  # 6 beats at 160 BPM, 0.5s per eighth
    note = pretty_midi.Note(velocity=60, pitch=42, start=i, end=i + 0.125)
    drums.notes.append(note)

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Write the MIDI file
# midi.write disabled
