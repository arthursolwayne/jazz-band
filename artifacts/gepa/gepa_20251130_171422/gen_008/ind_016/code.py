
import pretty_midi

# Create a MIDI file with 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define instruments
sax = pretty_midi.Instrument(program=66)       # Tenor sax
bass = pretty_midi.Instrument(program=33)      # Double bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Define drum notes (MIDI note numbers)
kick = 36
snare = 38
hihat = 42

# Bar 1: Little Ray (drums) only (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
def add_drums(start_time):
    for bar in range(1):
        for beat in range(4):
            time = start_time + beat * 0.375
            if beat == 0 or beat == 2:
                # Kick on beat 1 and 3
                drums.notes.append(pretty_midi.Note(velocity=100, pitch=kick, start=time, end=time + 0.125))
            if beat == 1 or beat == 3:
                # Snare on beat 2 and 4
                drums.notes.append(pretty_midi.Note(velocity=100, pitch=snare, start=time, end=time + 0.125))
            # Hihat on every eighth
            drums.notes.append(pretty_midi.Note(velocity=80, pitch=hihat, start=time, end=time + 0.125))

add_drums(0.0)  # Bar 1

# Bar 2: Full ensemble (1.5 - 3.0s)
# Saxophone motif: Dm7, start on D, then Bb, F, C (1st inversion)
# Rhythmic pattern: D on beat 1, Bb on "and" of 2, F on beat 3, C on "and" of 4

def add_sax(start_time):
    # Dm7: D, Bb, F, C
    # Time signatures: bar is 1.5s, beat is 0.375s
    # Note durations: 0.375s (quarter), 0.1875s (eighth)
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=start_time, end=start_time + 0.375))  # D
    sax.notes.append(pretty_midi.Note(velocity=105, pitch=60, start=start_time + 0.1875, end=start_time + 0.375))  # Bb (eighth note)
    sax.notes.append(pretty_midi.Note(velocity=105, pitch=57, start=start_time + 0.75, end=start_time + 1.125))  # F
    sax.notes.append(pretty_midi.Note(velocity=105, pitch=55, start=start_time + 0.9375, end=start_time + 1.125))  # C (eighth note)

add_sax(1.5)  # Bar 2

# Bass: Walking line with chromatic passing tones
def add_bass(start_time):
    # Dm7 walking line: D -> Eb -> F -> G -> A -> Bb -> C -> D
    # D (62), Eb (63), F (64), G (65), A (66), Bb (67), C (68), D (69)
    times = [start_time + 0.375 * i for i in range(8)]
    for i, pitch in enumerate([62, 63, 64, 65, 66, 67, 68, 69]):
        bass.notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=times[i], end=times[i] + 0.125))

add_bass(1.5)  # Bar 2

# Piano: Comping with 7th chords on 2 and 4
def add_piano(start_time):
    # Dm7 = D, F, A, C
    # Bb7 = Bb, D, F, Ab
    def play_chord(pitch_list, start_time):
        for pitch in pitch_list:
            piano.notes.append(pretty_midi.Note(velocity=95, pitch=pitch, start=start_time, end=start_time + 0.125))

    # 2nd beat (bar 2): Dm7
    play_chord([62, 64, 67, 59], start_time + 0.75)  # D, F, A, C (Dm7)
    # 4th beat (bar 2): Bb7
    play_chord([60, 62, 64, 58], start_time + 1.5)    # Bb, D, F, Ab (Bb7)

add_piano(1.5)  # Bar 2

# Bar 3: Continue the sax phrase, resolve on beat 4 with a C
def add_sax_bar3(start_time):
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=55, start=start_time + 1.5, end=start_time + 1.875))  # C on "and" of 4

add_sax_bar3(1.5)  # Bar 3

# Bar 4: Repeat the same sax motif but end on a C
def add_sax_bar4(start_time):
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=start_time, end=start_time + 0.375))  # D
    sax.notes.append(pretty_midi.Note(velocity=105, pitch=60, start=start_time + 0.1875, end=start_time + 0.375))  # Bb
    sax.notes.append(pretty_midi.Note(velocity=105, pitch=57, start=start_time + 0.75, end=start_time + 1.125))  # F
    sax.notes.append(pretty_midi.Note(velocity=105, pitch=55, start=start_time + 0.9375, end=start_time + 1.125))  # C
    sax.notes.append(pretty_midi.Note(velocity=105, pitch=55, start=start_time + 1.5, end=start_time + 1.875))  # C on "and" of 4

add_sax_bar4(3.0)  # Bar 4

# Bass: Continue walking line
def add_bass_bar3(start_time):
    times = [start_time + 0.375 * i for i in range(4)]
    for i, pitch in enumerate([69, 70, 71, 72]):
        bass.notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=times[i], end=times[i] + 0.125))

def add_bass_bar4(start_time):
    times = [start_time + 0.375 * i for i in range(4)]
    for i, pitch in enumerate([72, 69, 71, 72]):
        bass.notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=times[i], end=times[i] + 0.125))

add_bass_bar3(3.0)
add_bass_bar4(3.375)

# Piano: Comping again on 2 and 4 of bar 3 and 4
def add_piano_bar3(start_time):
    play_chord([62, 64, 67, 59], start_time + 0.75)  # Dm7
    play_chord([60, 62, 64, 58], start_time + 1.5)    # Bb7

def add_piano_bar4(start_time):
    play_chord([62, 64, 67, 59], start_time + 0.75)  # Dm7
    play_chord([60, 62, 64, 58], start_time + 1.5)    # Bb7

add_piano_bar3(3.0)
add_piano_bar4(3.375)

# Drums: Repeat pattern for bars 2-4 (1.5 - 6.0s)
def add_drums_bars2_4(start_time):
    for bar in range(3):  # Bars 2, 3, 4
        for beat in range(4):
            time = start_time + bar * 1.5 + beat * 0.375
            if beat == 0 or beat == 2:
                # Kick on beat 1 and 3
                drums.notes.append(pretty_midi.Note(velocity=100, pitch=kick, start=time, end=time + 0.125))
            if beat == 1 or beat == 3:
                # Snare on beat 2 and 4
                drums.notes.append(pretty_midi.Note(velocity=100, pitch=snare, start=time, end=time + 0.125))
            # Hihat on every eighth
            drums.notes.append(pretty_midi.Note(velocity=80, pitch=hihat, start=time, end=time + 0.125))

add_drums_bars2_4(1.5)  # Bars 2, 3, 4

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
print("MIDI file saved as 'dante_intro.mid'")
