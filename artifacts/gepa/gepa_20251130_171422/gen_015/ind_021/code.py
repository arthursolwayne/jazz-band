
import pretty_midi

# Create a new MIDI file
midi = pretty_midi.PrettyMIDI()
midi.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]
midi.key_signature_changes = [pretty_midi.KeySignature(-2, 0)]  # D minor
midi.instruments = []

# Set tempo to 160 BPM
midi.time_zone = 0
midi.tempo_changes = [pretty_midi.TempoChange(160, 0)]

# Create instruments
drums = pretty_midi.Instrument(program=12)
bass = pretty_midi.Instrument(program=33)
piano = pretty_midi.Note()
sax = pretty_midi.Instrument(program=64)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar = 1.5 seconds, beat = 0.375 seconds
# Total time: 6 seconds for 4 bars

# Hihat on every eighth note = 8 notes per bar
for bar in range(4):
    for note in range(8):
        time = bar * 1.5 + note * 0.375
        if note in [0, 4]:  # Kick on beat 1 and 3
            drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125))
        if note in [2, 6]:  # Snare on beat 2 and 4
            drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125))
        if note % 2 == 0:  # Hihat on every eighth
            drums.notes.append(pretty_midi.Note(velocity=60, pitch=42, start=time, end=time + 0.125))

# Bass: Walking line, chromatic approaches, never the same note twice
# Dm7 chord: D, F, A, C
# Start on C, then chromatic approach to D
bass_notes = [
    (0.0, 60),  # C
    (0.375, 61),  # C#
    (0.75, 62),  # D
    (1.125, 64),  # E
    (1.5, 65),  # F
    (1.875, 67),  # F#
    (2.25, 69),  # G
    (2.625, 70),  # G#
    (3.0, 72),  # A
    (3.375, 71),  # Ab (chromatic down to A)
    (3.75, 70),  # G#
    (4.125, 69),  # G
    (4.5, 67),  # F#
    (4.875, 65),  # F
    (5.25, 64),  # E
    (5.625, 62),  # D
]

for time, pitch in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.25))

# Piano: 7th chords, comp on 2 and 4
# Dm7 = D, F, A, C
# Am7 = A, C, E, G
# F7 = F, A, C, E♭
# Comping on beats 2 and 4
piano_notes = [
    # Bar 1
    (0.375, 62),  # A
    (0.375, 64),  # C
    (0.375, 67),  # E
    (0.375, 69),  # G

    # Bar 2
    (1.875, 65),  # F
    (1.875, 67),  # A
    (1.875, 69),  # C
    (1.875, 71),  # E♭

    # Bar 3
    (3.375, 62),  # A
    (3.375, 64),  # C
    (3.375, 67),  # E
    (3.375, 69),  # G

    # Bar 4
    (4.875, 65),  # F
    (4.875, 67),  # A
    (4.875, 69),  # C
    (4.875, 71),  # E♭
]

for time, pitch in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=time, end=time + 0.25))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Dm7 = D, F, A, C
# Motif: D (A), F (Bb), A (C), D (E) — a question, a challenge
# Let the motif start, end on the last beat, leave it hanging

sax_notes = [
    (0.0, 62),  # D
    (0.375, 64),  # F
    (0.75, 67),  # A
    (1.125, 69),  # C
    (1.5, 62),  # D
    (1.875, 64),  # F
    (2.25, 67),  # A
    (2.625, 69),  # C
    (3.0, 62),  # D
    (3.375, 64),  # F
    (3.75, 67),  # A
    (4.125, 69),  # C
    (4.5, 62),  # D
    (4.875, 64),  # F
    (5.25, 67),  # A
    (5.625, 69),  # C
]

for time, pitch in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.25))

# Add instruments to MIDI file
midi.instruments.append(drums)
midi.instruments.append(bass)
midi.instruments.append(piano)
midi.instruments.append(sax)

# Save the MIDI file
midi.write("dante_intro.mid")
