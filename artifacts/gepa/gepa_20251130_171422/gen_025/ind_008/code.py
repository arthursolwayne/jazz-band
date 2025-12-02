
import pretty_midi

# Create a new MIDI file with the specified tempo
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Instruments for the quartet
sax = pretty_midi.Instrument(program=66)       # Tenor sax
bass = pretty_midi.Instrument(program=33)      # Double bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Map drum notes (Standard MIDI percussion mapping)
DRUM_KICK = 36
DRUM_SNARE = 38
DRUM_HIHAT = 42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(1):
    # Each bar is 6 beats at 160 BPM = 1.5 seconds per bar
    # 6 beats = 6 * (60 / 160) = 2.25 seconds? Wait — no, 160 BPM is 160 beats per minute, so beat duration is 0.375s.
    # Bar duration = 4 beats = 1.5 seconds
    time = 0.0
    for beat in range(4):
        if beat == 0 or beat == 2:
            drums.notes.append(pretty_midi.Note(velocity=80, pitch=DRUM_KICK, start=time, end=time + 0.375))
        if beat == 1 or beat == 3:
            drums.notes.append(pretty_midi.Note(velocity=80, pitch=DRUM_SNARE, start=time, end=time + 0.375))
        # Hi-hat on every eighth note
        for eighth in range(2):
            drums.notes.append(pretty_midi.Note(velocity=70, pitch=DRUM_HIHAT, start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.1875))
        time += 0.375

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Time starts at 1.5 seconds

# Bass line: Walking line in Dm, chromatic approaches, no repeated notes
# Dm: D, F, A, C
# Walking bass line: D, F, Eb, G, A, Bb, C, D
bass_notes = [
    (1.5, 64),   # D
    (1.875, 65),  # F
    (2.25, 63),  # Eb
    (2.625, 67),  # G
    (3.0, 68),   # A
    (3.375, 66),  # Bb
    (3.75, 64),  # C
    (4.125, 64),  # D
    (4.5, 65),   # F
    (4.875, 63),  # Eb
    (5.25, 67),  # G
    (5.625, 68)  # A
]
for time, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.375))

# Piano: 7th chords, comp on 2 and 4
# Dm7: D, F, A, C
# Comp on beat 2 and 4 of each bar
chords = [
    (1.875, [64, 66, 68, 64]),  # Dm7
    (2.625, [64, 66, 68, 64]),  # Dm7
    (3.375, [64, 66, 68, 64]),  # Dm7
    (4.125, [64, 66, 68, 64]),  # Dm7
    (4.875, [64, 66, 68, 64]),  # Dm7
    (5.625, [64, 66, 68, 64])   # Dm7
]
for time, pitches in chords:
    for pitch in pitches:
        piano.notes.append(pretty_midi.Note(velocity=80, pitch=pitch, start=time, end=time + 0.375))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Dm: D, F, Ab, Bb
# Motif: D (beat 1), F (beat 2), Ab (beat 3), leave Bb hanging on beat 4
sax_notes = [
    (1.5, 64),   # D
    (1.875, 66),  # F
    (2.25, 68),  # Ab
    (2.625, 68)  # Bb (left hanging)
]
for time, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375))

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save to a file
midi.write("dante_intro.mid")
