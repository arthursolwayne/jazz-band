
import pretty_midi

# Create a PrettyMIDI object
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Set the key: D Major
key = 'D'

# Time signature: 4/4
time_signature = pretty_midi.TimeSignature(numerator=4, denominator=4, time=0)

# Add the time signature
midi.time_signature_changes.append(time_signature)

# Define the tempo
midi.tempo_changes.append(pretty_midi.TempoChange(160, 0))

# Create instruments
saxophone_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')
bass_program = pretty_midi.instrument_name_to_program('Acoustic Bass')
piano_program = pretty_midi.instrument_name_to_program('Electric Piano 1')
drums_program = pretty_midi.instrument_name_to_program('Drums')

sax = pretty_midi.Instrument(program=saxophone_program)
bass = pretty_midi.Instrument(program=bass_program)
piano = pretty_midi.Instrument(program=piano_program)
drums = pretty_midi.Instrument(program=drums_program)

# Add instruments to the MIDI file
midi.instruments.append(sax)
midi.instruments.append(bass)
midi.instruments.append(piano)
midi.instruments.append(drums)

# Define the time per beat and per bar
bpm = 160
seconds_per_beat = 60.0 / bpm
time_per_bar = 4 * seconds_per_beat  # 4/4 time

# Time for each bar
bar_1_time = 0.0
bar_2_time = bar_1_time + time_per_bar
bar_3_time = bar_2_time + time_per_bar
bar_4_time = bar_3_time + time_per_bar

#-------------------------- DRUMS (Little Ray) --------------------------
# Bar 1: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for beat in range(0, 4):
    time = bar_1_time + beat * seconds_per_beat
    if beat % 2 == 0:
        # Kick on 1 and 3
        kick = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.1)
        drums.notes.append(kick)
    else:
        # Snare on 2 and 4
        snare = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.1)
        drums.notes.append(snare)
    # Hihat on every eighth
    for subbeat in range(0, 2):
        hihat_time = time + subbeat * seconds_per_beat / 2
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=hihat_time, end=hihat_time + 0.05)
        drums.notes.append(hihat)

# Bars 2-4: Same pattern, just continue
for bar_start in [bar_2_time, bar_3_time, bar_4_time]:
    for beat in range(0, 4):
        time = bar_start + beat * seconds_per_beat
        if beat % 2 == 0:
            # Kick on 1 and 3
            kick = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.1)
            drums.notes.append(kick)
        else:
            # Snare on 2 and 4
            snare = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.1)
            drums.notes.append(snare)
        # Hihat on every eighth
        for subbeat in range(0, 2):
            hihat_time = time + subbeat * seconds_per_beat / 2
            hihat = pretty_midi.Note(velocity=80, pitch=42, start=hihat_time, end=hihat_time + 0.05)
            drums.notes.append(hihat)

#-------------------------- BASS (Marcus) --------------------------
# Walking line, chromatic approaches, no repeated notes
# Bar 1: D - C# - B - A
notes = [62, 61, 60, 59]  # D, C#, B, A
for i, note in enumerate(notes):
    start = bar_1_time + i * seconds_per_beat
    end = start + 0.25
    bass_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=end)
    bass.notes.append(bass_note)

# Bar 2: D - E - F# - G
notes = [62, 64, 66, 67]  # D, E, F#, G
for i, note in enumerate(notes):
    start = bar_2_time + i * seconds_per_beat
    end = start + 0.25
    bass_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=end)
    bass.notes.append(bass_note)

# Bar 3: A - B - C# - D
notes = [59, 60, 61, 62]  # A, B, C#, D
for i, note in enumerate(notes):
    start = bar_3_time + i * seconds_per_beat
    end = start + 0.25
    bass_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=end)
    bass.notes.append(bass_note)

# Bar 4: G - F# - E - D
notes = [67, 66, 64, 62]  # G, F#, E, D
for i, note in enumerate(notes):
    start = bar_4_time + i * seconds_per_beat
    end = start + 0.25
    bass_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=end)
    bass.notes.append(bass_note)

#-------------------------- PIANO (Diane) --------------------------
# 7th chords, comp on 2 and 4, staying out of the way

# Bar 1: Comp on 2 and 4 (Dmaj7 on beat 2, D7 on beat 4)
# Dmaj7: D, F#, A, C#
# D7: D, F#, A, C
# Voice leading: D -> D, F# -> F#, A -> A, C# -> C
chord_notes = [62, 66, 69, 71]  # Dmaj7
for i, note in enumerate(chord_notes):
    start = bar_1_time + 1 * seconds_per_beat  # beat 2
    end = start + 0.5
    piano_note = pretty_midi.Note(velocity=90, pitch=note, start=start, end=end)
    piano.notes.append(piano_note)

chord_notes = [62, 66, 69, 70]  # D7
for i, note in enumerate(chord_notes):
    start = bar_1_time + 3 * seconds_per_beat  # beat 4
    end = start + 0.5
    piano_note = pretty_midi.Note(velocity=90, pitch=note, start=start, end=end)
    piano.notes.append(piano_note)

# Bar 2: G7 on beat 2, A7 on beat 4
# G7: G, B, D, F
# A7: A, C#, E, G
chord_notes = [67, 71, 69, 65]  # G7
for i, note in enumerate(chord_notes):
    start = bar_2_time + 1 * seconds_per_beat  # beat 2
    end = start + 0.5
    piano_note = pretty_midi.Note(velocity=90, pitch=note, start=start, end=end)
    piano.notes.append(piano_note)

chord_notes = [69, 73, 71, 67]  # A7
for i, note in enumerate(chord_notes):
    start = bar_2_time + 3 * seconds_per_beat  # beat 4
    end = start + 0.5
    piano_note = pretty_midi.Note(velocity=90, pitch=note, start=start, end=end)
    piano.notes.append(piano_note)

# Bar 3: C7 on beat 2, D7 on beat 4
# C7: C, E, G, Bb
# D7: D, F#, A, C
chord_notes = [60, 64, 67, 69]  # C7
for i, note in enumerate(chord_notes):
    start = bar_3_time + 1 * seconds_per_beat  # beat 2
    end = start + 0.5
    piano_note = pretty_midi.Note(velocity=90, pitch=note, start=start, end=end)
    piano.notes.append(piano_note)

chord_notes = [62, 66, 69, 71]  # D7
for i, note in enumerate(chord_notes):
    start = bar_3_time + 3 * seconds_per_beat  # beat 4
    end = start + 0.5
    piano_note = pretty_midi.Note(velocity=90, pitch=note, start=start, end=end)
    piano.notes.append(piano_note)

# Bar 4: F7 on beat 2, G7 on beat 4
# F7: F, A, C, Eb
# G7: G, B, D, F
chord_notes = [65, 69, 62, 64]  # F7
for i, note in enumerate(chord_notes):
    start = bar_4_time + 1 * seconds_per_beat  # beat 2
    end = start + 0.5
    piano_note = pretty_midi.Note(velocity=90, pitch=note, start=start, end=end)
    piano.notes.append(piano_note)

chord_notes = [67, 71, 69, 65]  # G7
for i, note in enumerate(chord_notes):
    start = bar_4_time + 3 * seconds_per_beat  # beat 4
    end = start + 0.5
    piano_note = pretty_midi.Note(velocity=90, pitch=note, start=start, end=end)
    piano.notes.append(piano_note)

#-------------------------- SAX (You) --------------------------
# Four-bar intro: short motif, start it, leave it hanging, then finish it

# Bar 1: Start the motif
# D (62), F# (66), B (69), then cut off
note1 = pretty_midi.Note(velocity=110, pitch=62, start=bar_1_time + 0.1, end=bar_1_time + 0.4)
note2 = pretty_midi.Note(velocity=110, pitch=66, start=bar_1_time + 0.4, end=bar_1_time + 0.7)
note3 = pretty_midi.Note(velocity=110, pitch=69, start=bar_1_time + 0.7, end=bar_1_time + 1.0)
sax.notes.append(note1)
sax.notes.append(note2)
sax.notes.append(note3)

# Bar 2: continuation, but leave it hanging
note4 = pretty_midi.Note(velocity=110, pitch=62, start=bar_2_time + 0.1, end=bar_2_time + 0.4)
note5 = pretty_midi.Note(velocity=110, pitch=66, start=bar_2_time + 0.4, end=bar_2_time + 0.7)
note6 = pretty_midi.Note(velocity=110, pitch=69, start=bar_2_time + 0.7, end=bar_2_time + 1.0)
sax.notes.append(note4)
sax.notes.append(note5)
sax.notes.append(note6)

# Bar 3: Same pattern again, building tension
note7 = pretty_midi.Note(velocity=110, pitch=62, start=bar_3_time + 0.1, end=bar_3_time + 0.4)
note8 = pretty_midi.Note(velocity=110, pitch=66, start=bar_3_time + 0.4, end=bar_3_time + 0.7)
note9 = pretty_midi.Note(velocity=110, pitch=69, start=bar_3_time + 0.7, end=bar_3_time + 1.0)
sax.notes.append(note7)
sax.notes.append(note8)
sax.notes.append(note9)

# Bar 4: Finish the motif
note10 = pretty_midi.Note(velocity=110, pitch=62, start=bar_4_time + 0.1, end=bar_4_time + 0.4)
note11 = pretty_midi.Note(velocity=110, pitch=66, start=bar_4_time + 0.4, end=bar_4_time + 0.7)
note12 = pretty_midi.Note(velocity=110, pitch=69, start=bar_4_time + 0.7, end=bar_4_time + 1.0)
sax.notes.append(note10)
sax.notes.append(note11)
sax.notes.append(note12)

# Save the MIDI file
midi.write("jazz_intro.mid")
