
import pretty_midi

# Initialize the MIDI file with 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Instruments
sax = pretty_midi.Instrument(program=66)       # Tenor sax
bass = pretty_midi.Instrument(program=33)      # Double bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drum notes: kick=36, snare=38, hihat=42
kick = 36
snare = 38
hihat = 42

# Time in seconds per bar
bar_length = 1.5  # 160 BPM, 4/4 time
time = 0.0

# Bar 1 (0.0 - 1.5s): Little Ray alone
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for beat in range(4):  # 0, 1, 2, 3
    if beat % 2 == 0:  # kick on 1 and 3 (0 and 2)
        note = pretty_midi.Note(velocity=100, pitch=kick, start=time + beat * 0.375, end=time + beat * 0.375 + 0.125)
        drums.notes.append(note)
    if beat % 2 == 1:  # snare on 2 and 4 (1 and 3)
        note = pretty_midi.Note(velocity=100, pitch=snare, start=time + beat * 0.375, end=time + beat * 0.375 + 0.125)
        drums.notes.append(note)
    # Hihat on every eighth
    note = pretty_midi.Note(velocity=90, pitch=hihat, start=time + beat * 0.375, end=time + beat * 0.375 + 0.125)
    drums.notes.append(note)

time += bar_length

# Bar 2 (1.5 - 3.0s): Full quartet
# Bass: Walking line in D, roots and fifths with chromatic approaches
bass_notes = [62, 63, 66, 65]  # D2, D#2, F#2, F2
for i, pitch in enumerate(bass_notes):
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=time + i * 0.375, end=time + i * 0.375 + 0.125)
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: D7 (D, F#, A, C#), open voicing
piano_notes = [62, 65, 67, 69]  # D2, F#2, A2, C#3
for pitch in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.375)
    piano.notes.append(note)

# Sax: Motif - short, singable, start and leave it hanging
# D4 (62) -> F#4 (66) -> A4 (69) -> D5 (72) (half note)
# Play the first two notes in bar 2, leave the last two for bar 3
note = pretty_midi.Note(velocity=110, pitch=62, start=time, end=time + 0.375)
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=66, start=time, end=time + 0.375)
sax.notes.append(note)

time += bar_length

# Bar 3 (3.0 - 4.5s)
# Bass: Walking line
bass_notes = [67, 69, 66, 65]  # A2, B2, F#2, F2
for i, pitch in enumerate(bass_notes):
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=time + i * 0.375, end=time + i * 0.375 + 0.125)
    bass.notes.append(note)

# Piano: G7 (G, B, D, F#)
piano_notes = [67, 71, 69, 72]  # G2, B2, D3, F#3
for pitch in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.375)
    piano.notes.append(note)

# Sax: Finish the motif - A4 -> D5
note = pretty_midi.Note(velocity=110, pitch=69, start=time, end=time + 0.375)
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=72, start=time, end=time + 0.375)
sax.notes.append(note)

# Drums: Same pattern
for beat in range(4):
    if beat % 2 == 0:  # kick on 1 and 3 (0 and 2)
        note = pretty_midi.Note(velocity=100, pitch=kick, start=time + beat * 0.375, end=time + beat * 0.375 + 0.125)
        drums.notes.append(note)
    if beat % 2 == 1:  # snare on 2 and 4 (1 and 3)
        note = pretty_midi.Note(velocity=100, pitch=snare, start=time + beat * 0.375, end=time + beat * 0.375 + 0.125)
        drums.notes.append(note)
    # Hihat on every eighth
    note = pretty_midi.Note(velocity=90, pitch=hihat, start=time + beat * 0.375, end=time + beat * 0.375 + 0.125)
    drums.notes.append(note)

time += bar_length

# Bar 4 (4.5 - 6.0s)
# Bass: Walking line
bass_notes = [65, 67, 69, 67]  # F2, A2, B2, A2
for i, pitch in enumerate(bass_notes):
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=time + i * 0.375, end=time + i * 0.375 + 0.125)
    bass.notes.append(note)

# Piano: C7 (C, E, G, B)
piano_notes = [60, 64, 67, 71]  # C2, E2, G2, B2
for pitch in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.375)
    piano.notes.append(note)

# Sax: Silence for now, let the resolve happen
# Drums: Same pattern
for beat in range(4):
    if beat % 2 == 0:  # kick on 1 and 3 (0 and 2)
        note = pretty_midi.Note(velocity=100, pitch=kick, start=time + beat * 0.375, end=time + beat * 0.375 + 0.125)
        drums.notes.append(note)
    if beat % 2 == 1:  # snare on 2 and 4 (1 and 3)
        note = pretty_midi.Note(velocity=100, pitch=snare, start=time + beat * 0.375, end=time + beat * 0.375 + 0.125)
        drums.notes.append(note)
    # Hihat on every eighth
    note = pretty_midi.Note(velocity=90, pitch=hihat, start=time + beat * 0.375, end=time + beat * 0.375 + 0.125)
    drums.notes.append(note)

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
print("MIDI file saved as 'dante_intro.mid'")
