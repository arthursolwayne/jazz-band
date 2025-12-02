
import pretty_midi

# Create a new MIDI file with tempo set to 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define instruments
sax = pretty_midi.Instrument(program=66)       # Tenor sax
bass = pretty_midi.Instrument(program=33)      # Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drums: kick=36, snare=38, hihat=42
# Define note durations in seconds (based on 160 BPM, 4/4 time)
beat = 0.375  # 60 / 160 = 0.375 seconds per beat
bar = 1.5     # 4 beats per bar

# Bar 1: Little Ray (drums only) - 0.0 to 1.5 seconds
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.0 + beat))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=beat * 2, end=beat * 2 + beat))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=beat, end=beat + beat))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=beat * 3, end=beat * 3 + beat))

# Hi-hat on every eighth note
for i in range(8):
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=i * (beat / 2), end=i * (beat / 2) + (beat / 2)))

# Bar 2: Everyone enters (1.5 - 3.0 seconds)

# Sax: your motif (F - G - A - F, with a slight chromatic approach)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.5 + beat),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=1.5 + beat, end=1.5 + beat * 2),  # G
    pretty_midi.Note(velocity=100, pitch=66, start=1.5 + beat * 2, end=1.5 + beat * 3),  # F# (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=65, start=1.5 + beat * 3, end=1.5 + beat * 4)  # F
]
sax.notes.extend(sax_notes)

# Bass: walking line in F minor, chromatic approaches, no repeated notes
# F - G - Ab - A - Bb - B - C - Db - D - Eb - E - F
# Let's use F minor scale with some chromaticism

bass_notes = [
    pretty_midi.Note(velocity=100, pitch=46, start=1.5, end=1.5 + beat),  # F
    pretty_midi.Note(velocity=100, pitch=48, start=1.5 + beat, end=1.5 + beat * 2),  # G
    pretty_midi.Note(velocity=100, pitch=47, start=1.5 + beat * 2, end=1.5 + beat * 3),  # F#
    pretty_midi.Note(velocity=100, pitch=48, start=1.5 + beat * 3, end=1.5 + beat * 4),  # G
    pretty_midi.Note(velocity=100, pitch=45, start=1.5 + beat * 4, end=1.5 + beat * 5),  # E
    pretty_midi.Note(velocity=100, pitch=47, start=1.5 + beat * 5, end=1.5 + beat * 6),  # F#
    pretty_midi.Note(velocity=100, pitch=48, start=1.5 + beat * 6, end=1.5 + beat * 7),  # G
    pretty_midi.Note(velocity=100, pitch=49, start=1.5 + beat * 7, end=1.5 + beat * 8),  # A
    pretty_midi.Note(velocity=100, pitch=47, start=1.5 + beat * 8, end=1.5 + beat * 9),  # F#
    pretty_midi.Note(velocity=100, pitch=46, start=1.5 + beat * 9, end=1.5 + beat * 10),  # F
    pretty_midi.Note(velocity=100, pitch=48, start=1.5 + beat * 10, end=1.5 + beat * 11),  # G
    pretty_midi.Note(velocity=100, pitch=46, start=1.5 + beat * 11, end=1.5 + beat * 12),  # F
]
bass.notes.extend(bass_notes)

# Piano: 7th chords (F7, C7, G7, D7), comp on 2 and 4
# Bar 2: F7 on 2 and 4
piano_notes = []

# F7 on 2 and 4
for time in [beat, beat * 3]:
    piano_notes.append(pretty_midi.Note(velocity=90, pitch=64, start=time + 1.5, end=time + 1.5 + 0.25))  # F
    piano_notes.append(pretty_midi.Note(velocity=90, pitch=67, start=time + 1.5, end=time + 1.5 + 0.25))  # A
    piano_notes.append(pretty_midi.Note(velocity=90, pitch=69, start=time + 1.5, end=time + 1.5 + 0.25))  # C
    piano_notes.append(pretty_midi.Note(velocity=90, pitch=65, start=time + 1.5, end=time + 1.5 + 0.25))  # G (7th)

# Bar 3: C7 on 2 and 4
for time in [beat, beat * 3]:
    piano_notes.append(pretty_midi.Note(velocity=90, pitch=72, start=time + 1.5 + beat * 2, end=time + 1.5 + beat * 2 + 0.25))  # C
    piano_notes.append(pretty_midi.Note(velocity=90, pitch=75, start=time + 1.5 + beat * 2, end=time + 1.5 + beat * 2 + 0.25))  # E
    piano_notes.append(pretty_midi.Note(velocity=90, pitch=77, start=time + 1.5 + beat * 2, end=time + 1.5 + beat * 2 + 0.25))  # G
    piano_notes.append(pretty_midi.Note(velocity=90, pitch=74, start=time + 1.5 + beat * 2, end=time + 1.5 + beat * 2 + 0.25))  # Bb (7th)

# Bar 4: G7 on 2 and 4
for time in [beat, beat * 3]:
    piano_notes.append(pretty_midi.Note(velocity=90, pitch=76, start=time + 1.5 + beat * 4, end=time + 1.5 + beat * 4 + 0.25))  # G
    piano_notes.append(pretty_midi.Note(velocity=90, pitch=79, start=time + 1.5 + beat * 4, end=time + 1.5 + beat * 4 + 0.25))  # B
    piano_notes.append(pretty_midi.Note(velocity=90, pitch=81, start=time + 1.5 + beat * 4, end=time + 1.5 + beat * 4 + 0.25))  # D
    piano_notes.append(pretty_midi.Note(velocity=90, pitch=78, start=time + 1.5 + beat * 4, end=time + 1.5 + beat * 4 + 0.25))  # F# (7th)

piano.notes.extend(piano_notes)

# Bar 3: Little Ray (1.5 + beat * 2 to 1.5 + beat * 3)
# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.5 + beat * 2, end=1.5 + beat * 2 + beat))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.5 + beat * 4, end=1.5 + beat * 4 + beat))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=1.5 + beat * 3, end=1.5 + beat * 3 + beat))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=1.5 + beat * 5, end=1.5 + beat * 5 + beat))

# Hi-hat on every eighth
for i in range(8):
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=(i * (beat / 2)) + 1.5 + beat * 2, end=(i * (beat / 2)) + 1.5 + beat * 2 + (beat / 2)))

# Bar 4: Little Ray (1.5 + beat * 4 to 1.5 + beat * 6)
# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.5 + beat * 4, end=1.5 + beat * 4 + beat))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.5 + beat * 6, end=1.5 + beat * 6 + beat))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=1.5 + beat * 5, end=1.5 + beat * 5 + beat))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=1.5 + beat * 7, end=1.5 + beat * 7 + beat))

# Hi-hat on every eighth
for i in range(8):
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=(i * (beat / 2)) + 1.5 + beat * 4, end=(i * (beat / 2)) + 1.5 + beat * 4 + (beat / 2)))

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
