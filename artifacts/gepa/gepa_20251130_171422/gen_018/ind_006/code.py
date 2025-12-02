
import pretty_midi

# Create a new MIDI file with the specified tempo
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante - Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Marcus - Double Bass
piano = pretty_midi.Instrument(program=0)      # Diane - Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray - Drums

# Drum definitions
kick = 36
snare = 38
hihat = 42

# Time per bar at 160 BPM
bar_length = 60.0 / 160.0 * 4  # 6 seconds for 4 bars

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Drums only: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in [0]:
    start = bar * bar_length
    end = start + bar_length / 4  # 1.5s for 1 bar

    # Kick on 1 and 3
    kick_time = start
    kick_note = pretty_midi.Note(velocity=100, pitch=kick, start=kick_time, end=kick_time + 0.1)
    drums.notes.append(kick_note)

    kick_time = start + bar_length / 2
    kick_note = pretty_midi.Note(velocity=100, pitch=kick, start=kick_time, end=kick_time + 0.1)
    drums.notes.append(kick_note)

    # Snare on 2 and 4
    snare_time = start + bar_length / 4
    snare_note = pretty_midi.Note(velocity=100, pitch=snare, start=snare_time, end=snare_time + 0.1)
    drums.notes.append(snare_note)

    snare_time = start + bar_length * 3 / 4
    snare_note = pretty_midi.Note(velocity=100, pitch=snare, start=snare_time, end=snare_time + 0.1)
    drums.notes.append(snare_note)

    # Hihat on every eighth
    for i in range(8):
        hihat_time = start + i * (bar_length / 8)
        hihat_note = pretty_midi.Note(velocity=90, pitch=hihat, start=hihat_time, end=hihat_time + 0.05)
        drums.notes.append(hihat_note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Start with sax melody

# Sax: Short motif in F minor (F, Ab, Bb, D)
sax_notes = [
    (1.5, 77),  # F4
    (1.75, 70),  # Ab4
    (2.0, 71),  # Bb4
    (2.25, 74)  # D5
]

for time, pitch in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.25)
    sax.notes.append(note)

# Bass: Walking line in F minor (F, G, Ab, A)
bass_notes = [
    (1.5, 77),  # F3
    (1.75, 78),  # G3
    (2.0, 70),  # Ab3
    (2.25, 71)  # A3
]

for time, pitch in bass_notes:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=time, end=time + 0.25)
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4 (F7 on beat 2, Bb7 on beat 4)
piano_notes = [
    # F7 (F, A, C, Eb)
    (1.75, 77),  # F4
    (1.75, 82),  # A4
    (1.75, 79),  # C5
    (1.75, 76),  # Eb4

    # Bb7 (Bb, D, F, Ab)
    (2.25, 71),  # Bb4
    (2.25, 74),  # D5
    (2.25, 77),  # F5
    (2.25, 70),  # Ab4
]

for time, pitch in piano_notes:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=time, end=time + 0.25)
    piano.notes.append(note)

# Drums: Bar 2
# Kick on 1 and 3
kick_time = 1.5
kick_note = pretty_midi.Note(velocity=100, pitch=kick, start=kick_time, end=kick_time + 0.1)
drums.notes.append(kick_note)

kick_time = 1.5 + bar_length / 2
kick_note = pretty_midi.Note(velocity=100, pitch=kick, start=kick_time, end=kick_time + 0.1)
drums.notes.append(kick_note)

# Snare on 2 and 4
snare_time = 1.5 + bar_length / 4
snare_note = pretty_midi.Note(velocity=100, pitch=snare, start=snare_time, end=snare_time + 0.1)
drums.notes.append(snare_note)

snare_time = 1.5 + bar_length * 3 / 4
snare_note = pretty_midi.Note(velocity=100, pitch=snare, start=snare_time, end=snare_time + 0.1)
drums.notes.append(snare_note)

# Hihat on every eighth
for i in range(8):
    hihat_time = 1.5 + i * (bar_length / 8)
    hihat_note = pretty_midi.Note(velocity=90, pitch=hihat, start=hihat_time, end=hihat_time + 0.05)
    drums.notes.append(hihat_note)

# Bar 3: Repeat sax melody with variation (3.0 - 4.5s)
# Sax: Repeat motif, but pull the last note back slightly
sax_notes = [
    (3.0, 77),  # F4
    (3.25, 70),  # Ab4
    (3.5, 71),  # Bb4
    (3.75, 74)  # D5
]

for time, pitch in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.25)
    sax.notes.append(note)

# Bass: Walking line in F minor (F, G, Ab, A)
bass_notes = [
    (3.0, 77),  # F3
    (3.25, 78),  # G3
    (3.5, 70),  # Ab3
    (3.75, 71)  # A3
]

for time, pitch in bass_notes:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=time, end=time + 0.25)
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4 (F7 on beat 2, Bb7 on beat 4)
piano_notes = [
    # F7 (F, A, C, Eb)
    (3.25, 77),  # F4
    (3.25, 82),  # A4
    (3.25, 79),  # C5
    (3.25, 76),  # Eb4

    # Bb7 (Bb, D, F, Ab)
    (3.75, 71),  # Bb4
    (3.75, 74),  # D5
    (3.75, 77),  # F5
    (3.75, 70),  # Ab4
]

for time, pitch in piano_notes:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=time, end=time + 0.25)
    piano.notes.append(note)

# Drums: Bar 3
# Kick on 1 and 3
kick_time = 3.0
kick_note = pretty_midi.Note(velocity=100, pitch=kick, start=kick_time, end=kick_time + 0.1)
drums.notes.append(kick_note)

kick_time = 3.0 + bar_length / 2
kick_note = pretty_midi.Note(velocity=100, pitch=kick, start=kick_time, end=kick_time + 0.1)
drums.notes.append(kick_note)

# Snare on 2 and 4
snare_time = 3.0 + bar_length / 4
snare_note = pretty_midi.Note(velocity=100, pitch=snare, start=snare_time, end=snare_time + 0.1)
drums.notes.append(snare_note)

snare_time = 3.0 + bar_length * 3 / 4
snare_note = pretty_midi.Note(velocity=100, pitch=snare, start=snare_time, end=snare_time + 0.1)
drums.notes.append(snare_note)

# Hihat on every eighth
for i in range(8):
    hihat_time = 3.0 + i * (bar_length / 8)
    hihat_note = pretty_midi.Note(velocity=90, pitch=hihat, start=hihat_time, end=hihat_time + 0.05)
    drums.notes.append(hihat_note)

# Bar 4: Repeat sax melody with resolution (4.5 - 6.0s)
# Sax: Repeat motif, but resolve the D5 to F5 (resolve the tension)
sax_notes = [
    (4.5, 77),  # F4
    (4.75, 70),  # Ab4
    (5.0, 71),  # Bb4
    (5.25, 77)  # F5 (resolve D5 to F5)
]

for time, pitch in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.25)
    sax.notes.append(note)

# Bass: Walking line in F minor (F, G, Ab, A)
bass_notes = [
    (4.5, 77),  # F3
    (4.75, 78),  # G3
    (5.0, 70),  # Ab3
    (5.25, 71)  # A3
]

for time, pitch in bass_notes:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=time, end=time + 0.25)
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4 (F7 on beat 2, Bb7 on beat 4)
piano_notes = [
    # F7 (F, A, C, Eb)
    (4.75, 77),  # F4
    (4.75, 82),  # A4
    (4.75, 79),  # C5
    (4.75, 76),  # Eb4

    # Bb7 (Bb, D, F, Ab)
    (5.25, 71),  # Bb4
    (5.25, 74),  # D5
    (5.25, 77),  # F5
    (5.25, 70),  # Ab4
]

for time, pitch in piano_notes:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=time, end=time + 0.25)
    piano.notes.append(note)

# Drums: Bar 4
# Kick on 1 and 3
kick_time = 4.5
kick_note = pretty_midi.Note(velocity=100, pitch=kick, start=kick_time, end=kick_time + 0.1)
drums.notes.append(kick_note)

kick_time = 4.5 + bar_length / 2
kick_note = pretty_midi.Note(velocity=100, pitch=kick, start=kick_time, end=kick_time + 0.1)
drums.notes.append(kick_note)

# Snare on 2 and 4
snare_time = 4.5 + bar_length / 4
snare_note = pretty_midi.Note(velocity=100, pitch=snare, start=snare_time, end=snare_time + 0.1)
drums.notes.append(snare_note)

snare_time = 4.5 + bar_length * 3 / 4
snare_note = pretty_midi.Note(velocity=100, pitch=snare, start=snare_time, end=snare_time + 0.1)
drums.notes.append(snare_note)

# Hihat on every eighth
for i in range(8):
    hihat_time = 4.5 + i * (bar_length / 8)
    hihat_note = pretty_midi.Note(velocity=90, pitch=hihat, start=hihat_time, end=hihat_time + 0.05)
    drums.notes.append(hihat_note)

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
