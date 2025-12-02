
import pretty_midi

# Create a new MIDI file with a tempo of 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Instruments for the quartet
sax = pretty_midi.Instrument(program=66)       # Tenor sax
bass = pretty_midi.Instrument(program=33)      # Double bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drums: kick=36, snare=38, hihat=42
drum_notes = {
    'kick': 36,
    'snare': 38,
    'hihat': 42
}

# Time in seconds for each bar at 160 BPM
bar_length = 1.5  # seconds per bar

# BAR 1: Little Ray on drums only (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

# 1st beat (0.0s)
drums.notes.append(pretty_midi.Note(velocity=100, pitch=drum_notes['kick'], start=0.0, end=0.375))
# 2nd beat (0.375s)
drums.notes.append(pretty_midi.Note(velocity=100, pitch=drum_notes['snare'], start=0.375, end=0.75))
# 3rd beat (0.75s)
drums.notes.append(pretty_midi.Note(velocity=100, pitch=drum_notes['kick'], start=0.75, end=1.125))
# 4th beat (1.125s)
drums.notes.append(pretty_midi.Note(velocity=100, pitch=drum_notes['snare'], start=1.125, end=1.5))
# Hihat on every eighth
for i in range(0, 4):
    hihat_start = i * 0.375
    hihat_end = hihat_start + 0.125
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=drum_notes['hihat'], start=hihat_start, end=hihat_end))

# BAR 2: Full quartet starts (1.5 - 3.0s)

# Marcus (bass) - walking line in F minor with chromatic approaches
# F minor scale: F, Gb, G, Ab, A, Bb, B, C
# Chromatic approach to F: E, F
# F - Gb - G - Ab - A - Bb - B - C - F

# Walking bass line (bar 2)
bass_notes = [
    (1.5, 71),  # F (C4)
    (1.875, 69),  # Eb (E4)
    (2.25, 71),  # F
    (2.625, 72),  # Gb
    (3.0, 74),  # G
]

for start, pitch in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=pitch, start=start, end=start + 0.375))

# Diane (piano) - 7th chords on 2 and 4, comping
# Bar 2 - 4: F7 on beat 2, Am7 on beat 4
# F7 = F, A, C, Eb
# Am7 = A, C, Eb, G

# Beat 2 (1.875s): F7
piano_notes = [
    (1.875, 71),  # F
    (1.875, 75),  # A
    (1.875, 76),  # Bb
    (1.875, 72),  # C
]

# Beat 4 (3.0s): Am7
piano_notes.extend([
    (3.0, 77),  # A
    (3.0, 79),  # C
    (3.0, 81),  # Eb
    (3.0, 83),  # G
])

for start, pitch in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=start + 0.125))

# Dante (sax) - Melody: One short motif, starts on beat 1 of bar 2, ends hanging
# Motif: F, Gb, F (chromatic approach to F), A (a half-step above)
# F (Eb4), Gb (F4), F (Eb4), A (G4)

sax_notes = [
    (1.5, 71),  # F (Eb4)
    (1.875, 72),  # Gb (F4)
    (2.25, 71),  # F (Eb4)
    (2.625, 76),  # A (G4)
]

for start, pitch in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + 0.375))

# BAR 3: Full quartet (3.0 - 4.5s)

# Marcus - walking line continues
bass_notes = [
    (3.0, 76),  # Ab
    (3.375, 77),  # A
    (3.75, 79),  # Bb
    (4.125, 81),  # B
]

for start, pitch in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=pitch, start=start, end=start + 0.375))

# Diane - 7th chords again
# F7 on beat 2, Am7 on beat 4
piano_notes = [
    (3.875, 71),  # F
    (3.875, 75),  # A
    (3.875, 76),  # Bb
    (3.875, 72),  # C
]

# Beat 4 (4.5s): Am7
piano_notes.extend([
    (4.5, 77),  # A
    (4.5, 79),  # C
    (4.5, 81),  # Eb
    (4.5, 83),  # G
])

for start, pitch in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=start + 0.125))

# Dante - Motif repeats with variation
# F, Gb, Ab, Bb (chromatic line)
sax_notes = [
    (3.0, 71),  # F
    (3.375, 72),  # Gb
    (3.75, 74),  # Ab
    (4.125, 76),  # Bb
]

for start, pitch in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + 0.375))

# BAR 4: Full quartet (4.5 - 6.0s)

# Marcus - walking line
bass_notes = [
    (4.5, 81),  # B
    (4.875, 83),  # C
    (5.25, 71),  # F
    (5.625, 72),  # Gb
]

for start, pitch in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=pitch, start=start, end=start + 0.375))

# Diane - 7th chords
# F7 on beat 2, Am7 on beat 4
piano_notes = [
    (5.375, 71),  # F
    (5.375, 75),  # A
    (5.375, 76),  # Bb
    (5.375, 72),  # C
]

# Beat 4 (6.0s): Am7
piano_notes.extend([
    (6.0, 77),  # A
    (6.0, 79),  # C
    (6.0, 81),  # Eb
    (6.0, 83),  # G
])

for start, pitch in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=start + 0.125))

# Dante - Motif ends with a resolution
# F, Ab, C, F (resolve on F)
sax_notes = [
    (4.5, 71),  # F
    (4.875, 74),  # Ab
    (5.25, 76),  # C
    (5.625, 71),  # F
]

for start, pitch in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + 0.375))

# Drums continue in bar 3-4 with kick, snare, hihat

# BAR 3 (3.0 - 4.5s)
# Kick on 1 and 3, snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=drum_notes['kick'], start=3.0, end=3.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=drum_notes['snare'], start=3.375, end=3.75))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=drum_notes['kick'], start=3.75, end=4.125))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=drum_notes['snare'], start=4.125, end=4.5))

# Hihat on every eighth
for i in range(0, 4):
    hihat_start = 3.0 + i * 0.375
    hihat_end = hihat_start + 0.125
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=drum_notes['hihat'], start=hihat_start, end=hihat_end))

# BAR 4 (4.5 - 6.0s)
drums.notes.append(pretty_midi.Note(velocity=100, pitch=drum_notes['kick'], start=4.5, end=4.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=drum_notes['snare'], start=4.875, end=5.25))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=drum_notes['kick'], start=5.25, end=5.625))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=drum_notes['snare'], start=5.625, end=6.0))

# Hihat on every eighth
for i in range(0, 4):
    hihat_start = 4.5 + i * 0.375
    hihat_end = hihat_start + 0.125
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=drum_notes['hihat'], start=hihat_start, end=hihat_end))

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("4_bar_intro.mid")
