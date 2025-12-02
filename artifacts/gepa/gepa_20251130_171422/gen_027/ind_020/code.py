
import pretty_midi

# Initialize the MIDI file with tempo 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Create instruments for the quartet
sax = pretty_midi.Instrument(program=66)       # Tenor sax
bass = pretty_midi.Instrument(program=33)      # Double bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drum notes: kick=36, snare=38, hihat=42, ride=45, tom=47
drum_notes = {
    'kick': 36,
    'snare': 38,
    'hihat': 42,
    'ride': 45,
    'tom': 47
}

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Rhythmic question. Kick on 1 and 3, snare on 2 and 4, hihat on every eighth. But with subtle dynamics and tension.
bar_duration = 1.5  # 1 bar = 1.5 seconds
beat = bar_duration / 4  # 0.375 seconds per beat

# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(
    velocity=80, pitch=drum_notes['kick'], start=0.0, end=0.0 + beat
))
drums.notes.append(pretty_midi.Note(
    velocity=80, pitch=drum_notes['kick'], start=2 * beat, end=2 * beat + beat
))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(
    velocity=100, pitch=drum_notes['snare'], start=1 * beat, end=1 * beat + beat
))
drums.notes.append(pretty_midi.Note(
    velocity=100, pitch=drum_notes['snare'], start=3 * beat, end=3 * beat + beat
))

# Hihat on every eighth (for 4 beats)
for i in range(8):
    hihat_start = i * beat / 2
    drums.notes.append(pretty_midi.Note(
        velocity=80, pitch=drum_notes['hihat'], start=hihat_start, end=hihat_start + beat / 2
    ))

# Bar 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): Walking line, chromatic approaches, never the same note twice.
# Key: D minor (since the mood is dark, emotional, and introspective)
# D minor scale: D, Eb, F, G, Ab, Bb, C
# Let's use chromatic passing tones and a walking line in D minor

time = 1.5  # start of bar 2
bass_notes = [
    (D, time, time + beat),
    (Eb, time + beat, time + 2*beat),
    (F, time + 2*beat, time + 3*beat),
    (G, time + 3*beat, time + 4*beat),
    (Ab, time + 4*beat, time + 5*beat),
    (Bb, time + 5*beat, time + 6*beat),
    (C, time + 6*beat, time + 7*beat),
    (D, time + 7*beat, time + 8*beat),
]
for pitch, start, end in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=pitch, start=start, end=end))

# Piano (Diane): Comp on 2 and 4 with 7th chords, emotional and tense
# Dmin7 = D, F, Ab, C
# G7 = G, B, D, F
# Bb7 = Bb, D, F, Ab
# C7 = C, E, G, B

piano_notes = [
    # Bar 2, beat 2: Dmin7
    (D, time + beat, time + beat + beat),
    (F, time + beat, time + beat + beat),
    (Ab, time + beat, time + beat + beat),
    (C, time + beat, time + beat + beat),
    # Bar 2, beat 4: G7
    (G, time + 3*beat, time + 3*beat + beat),
    (B, time + 3*beat, time + 3*beat + beat),
    (D, time + 3*beat, time + 3*beat + beat),
    (F, time + 3*beat, time + 3*beat + beat),
    # Bar 3, beat 2: Bb7
    (Bb, time + 5*beat, time + 5*beat + beat),
    (D, time + 5*beat, time + 5*beat + beat),
    (F, time + 5*beat, time + 5*beat + beat),
    (Ab, time + 5*beat, time + 5*beat + beat),
    # Bar 3, beat 4: C7
    (C, time + 7*beat, time + 7*beat + beat),
    (E, time + 7*beat, time + 7*beat + beat),
    (G, time + 7*beat, time + 7*beat + beat),
    (B, time + 7*beat, time + 7*beat + beat),
]

for pitch, start, end in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=end))

# Drums continue: kick, snare, hihat
# Same pattern, but with a slight increase in velocity and a little more energy

# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(
    velocity=90, pitch=drum_notes['kick'], start=1.5, end=1.5 + beat
))
drums.notes.append(pretty_midi.Note(
    velocity=90, pitch=drum_notes['kick'], start=1.5 + 2 * beat, end=1.5 + 2 * beat + beat
))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(
    velocity=110, pitch=drum_notes['snare'], start=1.5 + beat, end=1.5 + beat + beat
))
drums.notes.append(pretty_midi.Note(
    velocity=110, pitch=drum_notes['snare'], start=1.5 + 3 * beat, end=1.5 + 3 * beat + beat
))

# Hihat on every eighth
for i in range(8):
    hihat_start = 1.5 + i * beat / 2
    drums.notes.append(pretty_midi.Note(
        velocity=85, pitch=drum_notes['hihat'], start=hihat_start, end=hihat_start + beat / 2
    ))

# Saxophone motif (Dante): short, emotional, incomplete at first, then resolved

# First bar (bar 2): 4 notes, delayed, spaced
# D, Eb, F, G — ascending but with tension
# Play on beats 2 and 4 in bar 2, then resolve in bar 4

# Bar 2, beat 2
sax.notes.append(pretty_midi.Note(
    velocity=105, pitch=D, start=1.5 + beat, end=1.5 + beat + beat / 2
))
# Bar 2, beat 4
sax.notes.append(pretty_midi.Note(
    velocity=105, pitch=G, start=1.5 + 3 * beat, end=1.5 + 3 * beat + beat / 2
))

# Bar 3, beat 2: Eb
sax.notes.append(pretty_midi.Note(
    velocity=105, pitch=Eb, start=1.5 + 5 * beat, end=1.5 + 5 * beat + beat / 2
))

# Bar 4, beat 4: F (resolution)
sax.notes.append(pretty_midi.Note(
    velocity=110, pitch=F, start=1.5 + 7 * beat, end=1.5 + 7 * beat + beat
))

# Add a little space, a rest after the resolution
# Let the note hang for a beat, then resolve it with a short C
sax.notes.append(pretty_midi.Note(
    velocity=100, pitch=C, start=1.5 + 7 * beat + beat / 2, end=1.5 + 7 * beat + beat / 2 + beat / 4
))

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write('dante_cellar_intro.mid')
