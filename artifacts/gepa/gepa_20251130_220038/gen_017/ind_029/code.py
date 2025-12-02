
import pretty_midi

# Create a new MIDI file with the specified tempo
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Create instruments for the quartet
sax = pretty_midi.Instrument(program=66)       # Tenor sax
bass = pretty_midi.Instrument(program=33)      # Double bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# MIDI note mappings for drums
kick = 36
snare = 38
hihat = 42

# Bar 1: Drums alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
bar_duration = 1.5  # 60 / 160 * 4 = 1.5s per bar

# Bar 1 (0.0 - 1.5s)
# Kick on 0.0 and 0.75s (beats 1 and 3)
kick_1 = pretty_midi.Note(velocity=100, pitch=kick, start=0.0, end=0.05)
kick_2 = pretty_midi.Note(velocity=100, pitch=kick, start=0.75, end=0.8)
drums.notes.extend([kick_1, kick_2])

# Snare on 0.375 and 1.125s (beats 2 and 4)
snare_1 = pretty_midi.Note(velocity=100, pitch=snare, start=0.375, end=0.4)
snare_2 = pretty_midi.Note(velocity=100, pitch=snare, start=1.125, end=1.15)
drums.notes.extend([snare_1, snare_2])

# Hihat on every eighth note
hihat_notes = [0.0, 0.375, 0.75, 1.125]
for t in hihat_notes:
    hihat_note = pretty_midi.Note(velocity=80, pitch=hihat, start=t, end=t + 0.05)
    drums.notes.append(hihat_note)

# Bar 2: Full ensemble (1.5 - 3.0s)

# Bass: Walking line, chromatic approaches
# Fm7 = F, Ab, C, Eb
# Walking line: F -> Gb -> G -> Ab -> Bb -> B -> C -> Db -> Eb
bass_notes = [
    (1.5, 71),  # F (71)
    (1.75, 69),  # Gb (69)
    (2.0, 71),  # G (71)
    (2.25, 69),  # Ab (69)
    (2.5, 67),  # Bb (67)
    (2.75, 65),  # B (65)
    (3.0, 67),  # C (67)
    (3.25, 64),  # Db (64)
    (3.5, 65)   # Eb (65)
]
for t, pitch in bass_notes:
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=t, end=t + 0.25)
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
# Fm7 = F, Ab, C, Eb
# Bar 2: Fm7 on beat 2 and 4 (1.75 and 3.0s)
chord = [71, 69, 67, 65]  # F, Ab, C, Eb
for t in [1.75, 3.0]:
    for pitch in chord:
        note = pretty_midi.Note(velocity=90, pitch=pitch, start=t, end=t + 0.25)
        piano.notes.append(note)

# Sax: Melody starts here
# Motif: F (71) -> Ab (69) -> C (67) -> Eb (65), then rest
sax_notes = [
    (1.5, 71),  # F
    (1.75, 69),  # Ab
    (2.0, 67),  # C
    (2.25, 65),  # Eb
]
for t, pitch in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=t, end=t + 0.25)
    sax.notes.append(note)

# Bar 3: Full ensemble (3.0 - 4.5s)

# Bass: Continue walking line
bass_notes = [
    (3.25, 64),  # Db
    (3.5, 65),  # Eb
    (3.75, 67),  # F
    (4.0, 69),  # Gb
    (4.25, 71),  # G
    (4.5, 69),  # Ab
    (4.75, 67),  # Bb
    (5.0, 65),  # B
    (5.25, 67),  # C
    (5.5, 64),  # Db
    (5.75, 65)   # Eb
]
for t, pitch in bass_notes:
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=t, end=t + 0.25)
    bass.notes.append(note)

# Piano: 7th chords again
# Fm7 on beat 2 and 4 (4.0 and 5.5s)
for t in [4.0, 5.5]:
    for pitch in chord:
        note = pretty_midi.Note(velocity=90, pitch=pitch, start=t, end=t + 0.25)
        piano.notes.append(note)

# Drums: Same pattern
# Kick on 3.0 and 3.75s (beats 1 and 3)
kick_1 = pretty_midi.Note(velocity=100, pitch=kick, start=3.0, end=3.05)
kick_2 = pretty_midi.Note(velocity=100, pitch=kick, start=3.75, end=3.8)
drums.notes.extend([kick_1, kick_2])

# Snare on 3.375 and 4.125s (beats 2 and 4)
snare_1 = pretty_midi.Note(velocity=100, pitch=snare, start=3.375, end=3.4)
snare_2 = pretty_midi.Note(velocity=100, pitch=snare, start=4.125, end=4.15)
drums.notes.extend([snare_1, snare_2])

# Hihat on every eighth note
hihat_notes = [3.0, 3.375, 3.75, 4.125]
for t in hihat_notes:
    hihat_note = pretty_midi.Note(velocity=80, pitch=hihat, start=t, end=t + 0.05)
    drums.notes.append(hihat_note)

# Bar 4: Full ensemble (4.5 - 6.0s)

# Sax: Return to the motif and finish it
sax_notes = [
    (4.5, 69),  # Ab
    (4.75, 67),  # C
    (5.0, 65),  # Eb
    (5.25, 67),  # C
    (5.5, 65),  # Eb
    (5.75, 67),  # C
    (6.0, 65)  # Eb
]
for t, pitch in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=t, end=t + 0.25)
    sax.notes.append(note)

# Bass: Continue walking line
bass_notes = [
    (6.0, 64),  # Db
    (6.25, 65),  # Eb
    (6.5, 67),  # F
    (6.75, 69),  # Gb
]
for t, pitch in bass_notes:
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=t, end=t + 0.25)
    bass.notes.append(note)

# Piano: 7th chords again
# Fm7 on beat 2 and 4 (5.5 and 6.75s)
for t in [5.5, 6.75]:
    for pitch in chord:
        note = pretty_midi.Note(velocity=90, pitch=pitch, start=t, end=t + 0.25)
        piano.notes.append(note)

# Drums: Same pattern
# Kick on 4.5 and 5.25s (beats 1 and 3)
kick_1 = pretty_midi.Note(velocity=100, pitch=kick, start=4.5, end=4.55)
kick_2 = pretty_midi.Note(velocity=100, pitch=kick, start=5.25, end=5.3)
drums.notes.extend([kick_1, kick_2])

# Snare on 4.875 and 5.625s (beats 2 and 4)
snare_1 = pretty_midi.Note(velocity=100, pitch=snare, start=4.875, end=4.9)
snare_2 = pretty_midi.Note(velocity=100, pitch=snare, start=5.625, end=5.65)
drums.notes.extend([snare_1, snare_2])

# Hihat on every eighth note
hihat_notes = [4.5, 4.875, 5.25, 5.625]
for t in hihat_notes:
    hihat_note = pretty_midi.Note(velocity=80, pitch=hihat, start=t, end=t + 0.05)
    drums.notes.append(hihat_note)

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_russo_intro.mid")
