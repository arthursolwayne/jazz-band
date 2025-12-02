
import pretty_midi

# Initialize the MIDI file
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Instruments
sax = pretty_midi.Instrument(program=66)         # Tenor sax
bass = pretty_midi.Instrument(program=33)        # Bass
piano = pretty_midi.Instrument(program=0)        # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drum note numbers
kick = 36
snare = 38
hihat = 42

# Time in seconds per bar (160 BPM, 4/4 time)
bar_length = 1.5

# BAR 1: Drums only (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every 8th
for i in range(2):  # 2 measures
    time = i * bar_length
    # Kick on beat 1 and 3
    kick_notes = [time, time + 0.75]
    for t in kick_notes:
        note = pretty_midi.Note(velocity=100, pitch=kick, start=t, end=t + 0.1)
        drums.notes.append(note)
    # Snare on beat 2 and 4
    snare_notes = [time + 0.5, time + 1.25]
    for t in snare_notes:
        note = pretty_midi.Note(velocity=100, pitch=snare, start=t, end=t + 0.1)
        drums.notes.append(note)
    # Hihat on every 8th
    for t in [time + 0.0, time + 0.25, time + 0.5, time + 0.75, time + 1.0, time + 1.25, time + 1.5, time + 1.75]:
        note = pretty_midi.Note(velocity=80, pitch=hihat, start=t, end=t + 0.05)
        drums.notes.append(note)

# BAR 2-4: Full quartet (1.5 - 6.0s)
# Key: Fm (F, Ab, Bb, C, Eb, G, A, C)

#------------- BASS LINE (Marcus) ------------------
# Walking line in Fm with chromatic approaches
bass_notes = [
    # Bar 2
    (1.5, 72),      # C (Fm7) - root
    (1.75, 69),     # Ab (chromatic approach)
    (2.0, 72),      # C (Fm7)
    (2.25, 69),     # Ab (chromatic approach)
    # Bar 3
    (2.5, 68),      # Bb (Fm7)
    (2.75, 65),     # G (chromatic)
    (3.0, 68),      # Bb (Fm7)
    (3.25, 65),     # G (chromatic)
    # Bar 4
    (3.5, 64),      # Eb (Fm7)
    (3.75, 62),     # D (chromatic)
    (4.0, 64),      # Eb (Fm7)
    (4.25, 62),     # D (chromatic)
]
for t, pitch in bass_notes:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=t, end=t + 0.25)
    bass.notes.append(note)

#------------- PIANO (Diane) ------------------
# Comping on 2 and 4 with 7th chords
# Fm7 = F, Ab, Bb, C (7th)
# Bb7 = Bb, D, F, Ab
# Eb7 = Eb, G, Bb, D
piano_notes = [
    # Bar 2
    (2.0, 64), (2.0, 69), (2.0, 71), (2.0, 72),  # Fm7
    # Bar 3
    (3.0, 71), (3.0, 74), (3.0, 64), (3.0, 69),  # Bb7
    # Bar 4
    (4.0, 63), (4.0, 67), (4.0, 71), (4.0, 74),  # Eb7
]
for t, pitch in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=t, end=t + 0.5)
    piano.notes.append(note)

#------------- SAX (Dante) ------------------
# A short, lyrical motif: F -> Ab -> Bb -> C (Fm7)
# Then take a breath, leave it hanging, come back
sax_notes = [
    # Bar 2
    (2.0, 72),     # F (octave 4)
    (2.15, 69),    # Ab
    (2.3, 71),     # Bb
    (2.45, 72),    # C (vibrato on this one)
    # Bar 3 (space)
    # Bar 4 (repeat motif with slight variation)
    (4.0, 72),     # F
    (4.15, 69),    # Ab
    (4.3, 71),     # Bb
    (4.45, 67),    # D (chromatic variation)
]
for t, pitch in sax_notes:
    note = pretty_midi.Note(velocity=105, pitch=pitch, start=t, end=t + 0.15)
    sax.notes.append(note)

#------------- DRUMS (Bars 2-4) ------------------
# Kick on 1 and 3, snare on 2 and 4, hihat on every 8th
for i in range(3):  # 3 measures
    time = 1.5 + i * bar_length
    # Kick on 1 and 3
    kick_notes = [time, time + 0.75]
    for t in kick_notes:
        note = pretty_midi.Note(velocity=100, pitch=kick, start=t, end=t + 0.1)
        drums.notes.append(note)
    # Snare on 2 and 4
    snare_notes = [time + 0.5, time + 1.25]
    for t in snare_notes:
        note = pretty_midi.Note(velocity=100, pitch=snare, start=t, end=t + 0.1)
        drums.notes.append(note)
    # Hihat on every 8th
    for t in [time + 0.0, time + 0.25, time + 0.5, time + 0.75, time + 1.0, time + 1.25, time + 1.5, time + 1.75]:
        note = pretty_midi.Note(velocity=80, pitch=hihat, start=t, end=t + 0.05)
        drums.notes.append(note)

# Add instruments to the MIDI file
midi.instruments = [sax, bass, piano, drums]

# Save the MIDI file
midi.write("dante_intro.mid")
