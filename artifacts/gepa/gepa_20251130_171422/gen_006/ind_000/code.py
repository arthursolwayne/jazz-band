
import pretty_midi

# Initialize the MIDI file with 160 BPM in 4/4 time
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Instruments
sax = pretty_midi.Instrument(program=66)       # Tenor sax
bass = pretty_midi.Instrument(program=33)      # Double bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drum note numbers
KICK = 36
SNARE = 38
HIHAT = 42

# Time in seconds for each bar (160 BPM, 4/4)
BAR_DURATION = 1.5  # 60 / 160 * 4 = 1.5
TIME_OFFSET = 0.0

# Bar 1: Drums only (0.0 - 1.5s)
# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for beat in [0, 1, 2, 3]:
    time = TIME_OFFSET + beat * 0.375  # 0.375s per beat
    if beat % 2 == 0:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=KICK, start=time, end=time + 0.125))
    else:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=SNARE, start=time, end=time + 0.125))
    # Hi-hat on every eighth
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=HIHAT, start=time, end=time + 0.125))

TIME_OFFSET += BAR_DURATION

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Chromatic walking line, never repeating a note
# Dorian mode in F: F, G, Ab, Bb, B, C, D
# Walking bass line: F, Gb, G, Ab, A, Bb, B, C, D, Eb, E, F
# Chromatic approach on each beat

bass_notes = [
    pretty_midi.Note(velocity=80, pitch=70, start=TIME_OFFSET, end=TIME_OFFSET + 0.375),  # F
    pretty_midi.Note(velocity=80, pitch=69, start=TIME_OFFSET + 0.375, end=TIME_OFFSET + 0.75),  # Gb
    pretty_midi.Note(velocity=80, pitch=71, start=TIME_OFFSET + 0.75, end=TIME_OFFSET + 1.125),  # G
    pretty_midi.Note(velocity=80, pitch=70, start=TIME_OFFSET + 1.125, end=TIME_OFFSET + 1.5),  # Ab
]

bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4 (F7, Bb7)
# Bar 2: F7 (F, A, C, Eb)
# Bar 2: comp on beat 2 and 4

# Beat 2 (0.75s)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=71, start=TIME_OFFSET + 0.75, end=TIME_OFFSET + 0.75 + 0.125),  # F
    pretty_midi.Note(velocity=90, pitch=74, start=TIME_OFFSET + 0.75, end=TIME_OFFSET + 0.75 + 0.125),  # A
    pretty_midi.Note(velocity=90, pitch=76, start=TIME_OFFSET + 0.75, end=TIME_OFFSET + 0.75 + 0.125),  # C
    pretty_midi.Note(velocity=90, pitch=73, start=TIME_OFFSET + 0.75, end=TIME_OFFSET + 0.75 + 0.125),  # Eb
]

# Beat 4 (1.5s)
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=74, start=TIME_OFFSET + 1.5, end=TIME_OFFSET + 1.5 + 0.125),  # Bb
    pretty_midi.Note(velocity=90, pitch=77, start=TIME_OFFSET + 1.5, end=TIME_OFFSET + 1.5 + 0.125),  # D
    pretty_midi.Note(velocity=90, pitch=76, start=TIME_OFFSET + 1.5, end=TIME_OFFSET + 1.5 + 0.125),  # C
    pretty_midi.Note(velocity=90, pitch=73, start=TIME_OFFSET + 1.5, end=TIME_OFFSET + 1.5 + 0.125),  # Eb
])

piano.notes.extend(piano_notes)

# Sax: Start the motif
# Motif: F (beat 1), Bb (beat 2, syncopated), C (beat 3), F (beat 4, held)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=TIME_OFFSET, end=TIME_OFFSET + 0.375),  # F
    pretty_midi.Note(velocity=100, pitch=73, start=TIME_OFFSET + 0.75, end=TIME_OFFSET + 1.125),  # Bb
    pretty_midi.Note(velocity=100, pitch=76, start=TIME_OFFSET + 1.125, end=TIME_OFFSET + 1.5),  # C
    pretty_midi.Note(velocity=100, pitch=71, start=TIME_OFFSET + 1.5, end=TIME_OFFSET + 1.5 + 0.375),  # F
]

sax.notes.extend(sax_notes)

# Drums: Same pattern for bar 2
for beat in [0, 1, 2, 3]:
    time = TIME_OFFSET + beat * 0.375
    if beat % 2 == 0:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=KICK, start=time, end=time + 0.125))
    else:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=SNARE, start=time, end=time + 0.125))
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=HIHAT, start=time, end=time + 0.125))

TIME_OFFSET += BAR_DURATION

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Continue chromatic walking
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=72, start=TIME_OFFSET, end=TIME_OFFSET + 0.375),  # A
    pretty_midi.Note(velocity=80, pitch=73, start=TIME_OFFSET + 0.375, end=TIME_OFFSET + 0.75),  # Bb
    pretty_midi.Note(velocity=80, pitch=74, start=TIME_OFFSET + 0.75, end=TIME_OFFSET + 1.125),  # B
    pretty_midi.Note(velocity=80, pitch=76, start=TIME_OFFSET + 1.125, end=TIME_OFFSET + 1.5),  # C
]

bass.notes.extend(bass_notes)

# Piano: Bb7 on beat 2 and 4
# Bb7: Bb, D, F, Ab
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=74, start=TIME_OFFSET + 0.75, end=TIME_OFFSET + 0.75 + 0.125),  # Bb
    pretty_midi.Note(velocity=90, pitch=77, start=TIME_OFFSET + 0.75, end=TIME_OFFSET + 0.75 + 0.125),  # D
    pretty_midi.Note(velocity=90, pitch=76, start=TIME_OFFSET + 0.75, end=TIME_OFFSET + 0.75 + 0.125),  # F
    pretty_midi.Note(velocity=90, pitch=73, start=TIME_OFFSET + 0.75, end=TIME_OFFSET + 0.75 + 0.125),  # Ab
]

# Beat 4
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=74, start=TIME_OFFSET + 1.5, end=TIME_OFFSET + 1.5 + 0.125),  # Bb
    pretty_midi.Note(velocity=90, pitch=77, start=TIME_OFFSET + 1.5, end=TIME_OFFSET + 1.5 + 0.125),  # D
    pretty_midi.Note(velocity=90, pitch=76, start=TIME_OFFSET + 1.5, end=TIME_OFFSET + 1.5 + 0.125),  # F
    pretty_midi.Note(velocity=90, pitch=73, start=TIME_OFFSET + 1.5, end=TIME_OFFSET + 1.5 + 0.125),  # Ab
])

piano.notes.extend(piano_notes)

# Sax: Continue the motif, embellish slightly
# F (beat 1), Bb (beat 2), Ab (beat 3), F (beat 4, held)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=TIME_OFFSET, end=TIME_OFFSET + 0.375),  # F
    pretty_midi.Note(velocity=100, pitch=73, start=TIME_OFFSET + 0.75, end=TIME_OFFSET + 1.125),  # Bb
    pretty_midi.Note(velocity=100, pitch=73, start=TIME_OFFSET + 1.125, end=TIME_OFFSET + 1.5),  # Ab
    pretty_midi.Note(velocity=100, pitch=71, start=TIME_OFFSET + 1.5, end=TIME_OFFSET + 1.5 + 0.375),  # F
]

sax.notes.extend(sax_notes)

# Drums: Same pattern
for beat in [0, 1, 2, 3]:
    time = TIME_OFFSET + beat * 0.375
    if beat % 2 == 0:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=KICK, start=time, end=time + 0.125))
    else:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=SNARE, start=time, end=time + 0.125))
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=HIHAT, start=time, end=time + 0.125))

TIME_OFFSET += BAR_DURATION

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Continue chromatic walking
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=77, start=TIME_OFFSET, end=TIME_OFFSET + 0.375),  # D
    pretty_midi.Note(velocity=80, pitch=76, start=TIME_OFFSET + 0.375, end=TIME_OFFSET + 0.75),  # C
    pretty_midi.Note(velocity=80, pitch=75, start=TIME_OFFSET + 0.75, end=TIME_OFFSET + 1.125),  # B
    pretty_midi.Note(velocity=80, pitch=74, start=TIME_OFFSET + 1.125, end=TIME_OFFSET + 1.5),  # Bb
]

bass.notes.extend(bass_notes)

# Piano: F7 on beat 2 and 4 again
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=71, start=TIME_OFFSET + 0.75, end=TIME_OFFSET + 0.75 + 0.125),  # F
    pretty_midi.Note(velocity=90, pitch=74, start=TIME_OFFSET + 0.75, end=TIME_OFFSET + 0.75 + 0.125),  # A
    pretty_midi.Note(velocity=90, pitch=76, start=TIME_OFFSET + 0.75, end=TIME_OFFSET + 0.75 + 0.125),  # C
    pretty_midi.Note(velocity=90, pitch=73, start=TIME_OFFSET + 0.75, end=TIME_OFFSET + 0.75 + 0.125),  # Eb
]

# Beat 4
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=74, start=TIME_OFFSET + 1.5, end=TIME_OFFSET + 1.5 + 0.125),  # Bb
    pretty_midi.Note(velocity=90, pitch=77, start=TIME_OFFSET + 1.5, end=TIME_OFFSET + 1.5 + 0.125),  # D
    pretty_midi.Note(velocity=90, pitch=76, start=TIME_OFFSET + 1.5, end=TIME_OFFSET + 1.5 + 0.125),  # C
    pretty_midi.Note(velocity=90, pitch=73, start=TIME_OFFSET + 1.5, end=TIME_OFFSET + 1.5 + 0.125),  # Eb
])

piano.notes.extend(piano_notes)

# Sax: Finish the motif, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=TIME_OFFSET, end=TIME_OFFSET + 0.375),  # F
    pretty_midi.Note(velocity=100, pitch=73, start=TIME_OFFSET + 0.75, end=TIME_OFFSET + 1.125),  # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=TIME_OFFSET + 1.125, end=TIME_OFFSET + 1.5),  # F
    pretty_midi.Note(velocity=100, pitch=71, start=TIME_OFFSET + 1.5, end=TIME_OFFSET + 1.5 + 0.375),  # F (held)
]

sax.notes.extend(sax_notes)

# Drums: Same pattern
for beat in [0, 1, 2, 3]:
    time = TIME_OFFSET + beat * 0.375
    if beat % 2 == 0:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=KICK, start=time, end=time + 0.125))
    else:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=SNARE, start=time, end=time + 0.125))
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=HIHAT, start=time, end=time + 0.125))

# Add instruments to MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
