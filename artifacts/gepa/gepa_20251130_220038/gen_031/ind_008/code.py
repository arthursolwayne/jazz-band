
import pretty_midi

# Create a new MIDI object with tempo of 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define the instruments
sax = pretty_midi.Instrument(program=66)       # Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Double Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Define drum note numbers
KICK = 36
SNARE = 38
HIHAT = 42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
bar1_start = 0.0
bar1_end = 1.5

# Kick on beat 1 and 3
kick_times = [bar1_start + 0.0, bar1_start + 0.75]
for t in kick_times:
    note = pretty_midi.Note(velocity=100, pitch=KICK, start=t, end=t + 0.1)
    drums.notes.append(note)

# Snare on beat 2 and 4
snare_times = [bar1_start + 0.375, bar1_start + 1.125]
for t in snare_times:
    note = pretty_midi.Note(velocity=100, pitch=SNARE, start=t, end=t + 0.1)
    drums.notes.append(note)

# Hi-hat on every eighth note
hihat_times = [bar1_start + 0.0, bar1_start + 0.375, bar1_start + 0.75, bar1_start + 1.125]
for t in hihat_times:
    note = pretty_midi.Note(velocity=100, pitch=HIHAT, start=t, end=t + 0.1)
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
bar2_start = 1.5
bar2_end = 3.0

# Saxophone motif (D, F#, A, B, D)
sax_notes = [62, 67, 70, 71, 62]  # D4, F#4, A4, B4, D4
sax_times = [bar2_start + 0.0, bar2_start + 0.125, bar2_start + 0.25, bar2_start + 0.375, bar2_start + 0.5]
for t, p in zip(sax_times, sax_notes):
    note = pretty_midi.Note(velocity=100, pitch=p, start=t, end=t + 0.1)
    sax.notes.append(note)

# Bass walking line: D, C#, B, A, G, F#, E, D
bass_notes = [62, 61, 60, 59, 58, 57, 56, 62]
bass_times = [bar2_start + 0.0, bar2_start + 0.125, bar2_start + 0.25, bar2_start + 0.375,
              bar2_start + 0.5, bar2_start + 0.625, bar2_start + 0.75, bar2_start + 1.0]
for t, p in zip(bass_times, bass_notes):
    note = pretty_midi.Note(velocity=80, pitch=p, start=t, end=t + 0.1)
    bass.notes.append(note)

# Piano chords: D7 on 2 and 4
piano_notes = [62, 67, 71, 72]  # D, F#, A, B (D7)
piano_times = [bar2_start + 0.375, bar2_start + 1.125]
for t in piano_times:
    for p in piano_notes:
        note = pretty_midi.Note(velocity=90, pitch=p, start=t, end=t + 0.1)
        piano.notes.append(note)

# Drums in bar 2: same pattern as bar 1
kick_times = [bar2_start + 0.0, bar2_start + 0.75]
for t in kick_times:
    note = pretty_midi.Note(velocity=100, pitch=KICK, start=t, end=t + 0.1)
    drums.notes.append(note)

snare_times = [bar2_start + 0.375, bar2_start + 1.125]
for t in snare_times:
    note = pretty_midi.Note(velocity=100, pitch=SNARE, start=t, end=t + 0.1)
    drums.notes.append(note)

hihat_times = [bar2_start + 0.0, bar2_start + 0.375, bar2_start + 0.75, bar2_start + 1.125]
for t in hihat_times:
    note = pretty_midi.Note(velocity=100, pitch=HIHAT, start=t, end=t + 0.1)
    drums.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
bar3_start = 3.0
bar3_end = 4.5

# Saxophone motif repeated, ending on B
sax_notes = [71, 62]  # B4, D4
sax_times = [bar3_start + 0.0, bar3_start + 0.5]
for t, p in zip(sax_times, sax_notes):
    note = pretty_midi.Note(velocity=100, pitch=p, start=t, end=t + 0.1)
    sax.notes.append(note)

# Bass walking line: D, C#, B, A, G, F#, E, D
bass_notes = [62, 61, 60, 59, 58, 57, 56, 62]
bass_times = [bar3_start + 0.0, bar3_start + 0.125, bar3_start + 0.25, bar3_start + 0.375,
              bar3_start + 0.5, bar3_start + 0.625, bar3_start + 0.75, bar3_start + 1.0]
for t, p in zip(bass_times, bass_notes):
    note = pretty_midi.Note(velocity=80, pitch=p, start=t, end=t + 0.1)
    bass.notes.append(note)

# Piano chords: D7 on 2 and 4
piano_notes = [62, 67, 71, 72]  # D, F#, A, B (D7)
piano_times = [bar3_start + 0.375, bar3_start + 1.125]
for t in piano_times:
    for p in piano_notes:
        note = pretty_midi.Note(velocity=90, pitch=p, start=t, end=t + 0.1)
        piano.notes.append(note)

# Drums in bar 3: same pattern as bar 1 and 2
kick_times = [bar3_start + 0.0, bar3_start + 0.75]
for t in kick_times:
    note = pretty_midi.Note(velocity=100, pitch=KICK, start=t, end=t + 0.1)
    drums.notes.append(note)

snare_times = [bar3_start + 0.375, bar3_start + 1.125]
for t in snare_times:
    note = pretty_midi.Note(velocity=100, pitch=SNARE, start=t, end=t + 0.1)
    drums.notes.append(note)

hihat_times = [bar3_start + 0.0, bar3_start + 0.375, bar3_start + 0.75, bar3_start + 1.125]
for t in hihat_times:
    note = pretty_midi.Note(velocity=100, pitch=HIHAT, start=t, end=t + 0.1)
    drums.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
bar4_start = 4.5
bar4_end = 6.0

# Saxophone motif: D, F#, A, B, D (ending on D)
sax_notes = [62, 67, 70, 71, 62]
sax_times = [bar4_start + 0.0, bar4_start + 0.125, bar4_start + 0.25, bar4_start + 0.375, bar4_start + 0.5]
for t, p in zip(sax_times, sax_notes):
    note = pretty_midi.Note(velocity=100, pitch=p, start=t, end=t + 0.1)
    sax.notes.append(note)

# Bass walking line: D, C#, B, A, G, F#, E, D
bass_notes = [62, 61, 60, 59, 58, 57, 56, 62]
bass_times = [bar4_start + 0.0, bar4_start + 0.125, bar4_start + 0.25, bar4_start + 0.375,
              bar4_start + 0.5, bar4_start + 0.625, bar4_start + 0.75, bar4_start + 1.0]
for t, p in zip(bass_times, bass_notes):
    note = pretty_midi.Note(velocity=80, pitch=p, start=t, end=t + 0.1)
    bass.notes.append(note)

# Piano chords: D7 on 2 and 4
piano_notes = [62, 67, 71, 72]  # D, F#, A, B (D7)
piano_times = [bar4_start + 0.375, bar4_start + 1.125]
for t in piano_times:
    for p in piano_notes:
        note = pretty_midi.Note(velocity=90, pitch=p, start=t, end=t + 0.1)
        piano.notes.append(note)

# Drums in bar 4: same pattern as bar 1, 2, 3
kick_times = [bar4_start + 0.0, bar4_start + 0.75]
for t in kick_times:
    note = pretty_midi.Note(velocity=100, pitch=KICK, start=t, end=t + 0.1)
    drums.notes.append(note)

snare_times = [bar4_start + 0.375, bar4_start + 1.125]
for t in snare_times:
    note = pretty_midi.Note(velocity=100, pitch=SNARE, start=t, end=t + 0.1)
    drums.notes.append(note)

hihat_times = [bar4_start + 0.0, bar4_start + 0.375, bar4_start + 0.75, bar4_start + 1.125]
for t in hihat_times:
    note = pretty_midi.Note(velocity=100, pitch=HIHAT, start=t, end=t + 0.1)
    drums.notes.append(note)

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_russo_intro.mid")
