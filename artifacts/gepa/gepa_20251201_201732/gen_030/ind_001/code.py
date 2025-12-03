
import pretty_midi

# Initialize the MIDI file with the specified tempo
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define instruments for each player
sax = pretty_midi.Instrument(program=66)       # Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Double Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drums: kick=36, snare=38, hihat=42
kick = 36
snare = 38
hihat = 42

# Time signature and tempo
time_signature = (4, 4)
note_length = 0.375  # 160 BPM, quarter note = 0.375s
bar_length = 1.5     # 4 bars = 6.0s, so 1 bar = 1.5s

# Bar 1: Drums alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for i in range(4):
    time = i * note_length
    if i % 2 == 0:  # Kick on 1 and 3 (0 and 2)
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=kick, start=time, end=time + note_length))
    else:  # Snare on 2 and 4 (1 and 3)
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=snare, start=time, end=time + note_length))
    # Hihat on every eighth
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=hihat, start=time, end=time + note_length / 2))
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=hihat, start=time + note_length / 2, end=time + note_length))

# Bar 2: Full ensemble (1.5 - 3.0s)
# Bass: Walking line in Dm, roots and fifths with chromatic approaches
# Dm: D, F, A, C
# Walking bass pattern: D -> Eb -> F -> G -> A -> Bb -> B -> C -> D
bass_notes = [62, 63, 65, 67, 69, 70, 71, 72, 62]
for i, note in enumerate(bass_notes):
    time = 1.5 + i * note_length
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + note_length))
    if i == len(bass_notes) - 1:
        break

# Piano: Open voicings, each bar a different chord, resolve on the last
# Bar 2: Dm7
piano_notes = [62, 67, 70, 72]  # D F A C
for note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=1.5, end=1.5 + note_length))

# Sax: Melody starts here — simple motif, one phrase, leave it hanging
# Dm7: D F A C
# Motif: D -> F -> D -> (pause)
sax_notes = [62, 65, 62]
for i, note in enumerate(sax_notes):
    time = 1.5 + i * note_length
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + note_length))
# Leave the last note hanging — not resolved yet
# D is the note, hang it for the full bar
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=1.5 + note_length, end=3.0))

# Bar 3: Full ensemble (3.0 - 4.5s)
# Bass: Continue walking
# Bar 3: Dm7 -> Gm7 (key change is not used, so back to Dm7)
# But for variation, use Cm7 and Gm7 to imply a ii-V
bass_notes = [60, 62, 65, 67, 69, 70, 71, 72, 62]
for i, note in enumerate(bass_notes):
    time = 3.0 + i * note_length
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + note_length))
    if i == len(bass_notes) - 1:
        break

# Piano: Cm7 (C Eb G Bb)
piano_notes = [60, 64, 67, 71]
for note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=3.0, end=3.0 + note_length))

# Sax: Continue the motif, but now resolve it
# D -> F -> D -> F -> C (resolve on C)
sax_notes = [65, 62, 65, 60]
for i, note in enumerate(sax_notes):
    time = 3.0 + i * note_length
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + note_length))

# Bar 4: Full ensemble (4.5 - 6.0s)
# Bass: Dm7 again, with chromatic approach to D
bass_notes = [63, 62, 65, 67, 69, 70, 71, 72, 62]
for i, note in enumerate(bass_notes):
    time = 4.5 + i * note_length
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + note_length))
    if i == len(bass_notes) - 1:
        break

# Piano: Dm7 (D F A C)
piano_notes = [62, 67, 70, 72]
for note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=4.5, end=4.5 + note_length))

# Sax: Final notes — resolve the motif
# F -> C (resolve on C), leave it hanging again
sax_notes = [65, 60]
for i, note in enumerate(sax_notes):
    time = 4.5 + i * note_length
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + note_length))
# Hang C for the full bar
sax.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=4.5 + note_length, end=6.0))

# Add the instruments to the MIDI file
midi.instruments.append(sax)
midi.instruments.append(bass)
midi.instruments.append(piano)
midi.instruments.append(drums)

# Save the MIDI file
# midi.write disabled
