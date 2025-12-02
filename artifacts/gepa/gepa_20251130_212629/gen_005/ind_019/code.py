
import pretty_midi

# Set up the MIDI file
midi = pretty_midi.PrettyMIDI()
midi.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]
midi.tempo_changes = [pretty_midi.TempoChange(160, 0)]

# Create instruments
drums = pretty_midi.Instrument(program=0)
bass = pretty_midi.Instrument(program=33)
piano = pretty_midi.Instrument(program=0)  # change to 42 for acoustic piano if needed
sax = pretty_midi.Instrument(program=64)

# Add instruments to MIDI
midi.instruments = [drums, bass, piano, sax]

# Constants
BPM = 160
BEAT = 60.0 / BPM  # seconds per beat
BAR = 4 * BEAT  # 4 beats per bar

# Bar 1: Little Ray (drums) alone
# Kick on 1 and 3, snare on 2 and 4, hihat on every 8th
for beat in [0, 1, 2, 3]:
    # Kick on 1 and 3
    if beat in [0, 2]:
        note = pretty_midi.Note(velocity=100, pitch=36, start=beat * BEAT, end=(beat + 0.05) * BEAT)
        drums.notes.append(note)
    # Snare on 2 and 4
    if beat in [1, 3]:
        note = pretty_midi.Note(velocity=100, pitch=38, start=beat * BEAT, end=(beat + 0.05) * BEAT)
        drums.notes.append(note)
    # Hi-hat on every 8th
    for i in range(2):
        note = pretty_midi.Note(velocity=70, pitch=42, start=(beat * 2 + i) * BEAT / 2, end=(beat * 2 + i + 0.05) * BEAT / 2)
        drums.notes.append(note)

# Bar 2-4: Everyone in. You (sax) take the melody
# Key: Dm (D Dorian or D Aeolian)
# Dm7 = D, F, A, C
# Start with a short motif: D - F - A - C (with some chromaticism and space)
# [D, F, A, C] -> [D, F, Bb, C] -> [D, F, A, C] -> [C, Bb, A, D]

# Bar 2: D, F, Bb, C
# Time: 0 to BAR
for beat in range(4):
    time = beat * BEAT
    if beat == 0:
        note = pretty_midi.Note(velocity=100, pitch=62, start=time, end=time + 0.25 * BEAT)
        sax.notes.append(note)
    elif beat == 1:
        note = pretty_midi.Note(velocity=100, pitch=65, start=time, end=time + 0.25 * BEAT)
        sax.notes.append(note)
    elif beat == 2:
        note = pretty_midi.Note(velocity=100, pitch=60, start=time, end=time + 0.25 * BEAT)
        sax.notes.append(note)
    elif beat == 3:
        note = pretty_midi.Note(velocity=100, pitch=64, start=time, end=time + 0.25 * BEAT)
        sax.notes.append(note)

# Bar 3: D, F, A, C
# Time: BAR to 2 * BAR
for beat in range(4):
    time = (beat + 1) * BEAT
    if beat == 0:
        note = pretty_midi.Note(velocity=100, pitch=62, start=time, end=time + 0.25 * BEAT)
        sax.notes.append(note)
    elif beat == 1:
        note = pretty_midi.Note(velocity=100, pitch=65, start=time, end=time + 0.25 * BEAT)
        sax.notes.append(note)
    elif beat == 2:
        note = pretty_midi.Note(velocity=100, pitch=67, start=time, end=time + 0.25 * BEAT)
        sax.notes.append(note)
    elif beat == 3:
        note = pretty_midi.Note(velocity=100, pitch=64, start=time, end=time + 0.25 * BEAT)
        sax.notes.append(note)

# Bar 4: C, Bb, A, D
# Time: 2 * BAR to 3 * BAR
for beat in range(4):
    time = (beat + 2) * BEAT
    if beat == 0:
        note = pretty_midi.Note(velocity=100, pitch=64, start=time, end=time + 0.25 * BEAT)
        sax.notes.append(note)
    elif beat == 1:
        note = pretty_midi.Note(velocity=100, pitch=62, start=time, end=time + 0.25 * BEAT)
        sax.notes.append(note)
    elif beat == 2:
        note = pretty_midi.Note(velocity=100, pitch=67, start=time, end=time + 0.25 * BEAT)
        sax.notes.append(note)
    elif beat == 3:
        note = pretty_midi.Note(velocity=100, pitch=62, start=time, end=time + 0.25 * BEAT)
        sax.notes.append(note)

# Bass: Walking line with chromatic approaches
# Dm7 walking line (D, F, A, C) - chromatic approach on 2nd beat
bass_notes = [
    # Bar 1
    (0, 62), (1, 60), (2, 64), (3, 62),
    # Bar 2
    (4, 62), (5, 60), (6, 64), (7, 62),
    # Bar 3
    (8, 62), (9, 60), (10, 64), (11, 62),
    # Bar 4
    (12, 62), (13, 60), (14, 64), (15, 62)
]

for i, (beat, pitch) in enumerate(bass_notes):
    time = beat * BEAT
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=time, end=time + 0.25 * BEAT)
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4, comp on 2 and 4
# Dm7 = D, F, A, C
# F7 = F, A, C, E
# A7 = A, C, E, G
# Cm7 = C, Eb, G, Bb

# Bar 1: No piano
# Bar 2: F7 on 2 (beat 1), Dm7 on 4 (beat 3)
for beat in [1, 3]:
    if beat == 1:
        # F7: F, A, C, E
        for pitch in [65, 68, 72, 74]:
            note = pretty_midi.Note(velocity=100, pitch=pitch, start=beat * BEAT, end=beat * BEAT + 0.25 * BEAT)
            piano.notes.append(note)
    elif beat == 3:
        # Dm7: D, F, A, C
        for pitch in [62, 65, 67, 64]:
            note = pretty_midi.Note(velocity=100, pitch=pitch, start=beat * BEAT, end=beat * BEAT + 0.25 * BEAT)
            piano.notes.append(note)

# Bar 3: A7 on 2 (beat 1), Cm7 on 4 (beat 3)
for beat in [1, 3]:
    if beat == 1:
        # A7: A, C, E, G
        for pitch in [67, 72, 76, 71]:
            note = pretty_midi.Note(velocity=100, pitch=pitch, start=beat * BEAT + BAR, end=beat * BEAT + BAR + 0.25 * BEAT)
            piano.notes.append(note)
    elif beat == 3:
        # Cm7: C, Eb, G, Bb
        for pitch in [64, 66, 71, 62]:
            note = pretty_midi.Note(velocity=100, pitch=pitch, start=beat * BEAT + BAR, end=beat * BEAT + BAR + 0.25 * BEAT)
            piano.notes.append(note)

# Bar 4: Dm7 on 2 (beat 1), F7 on 4 (beat 3)
for beat in [1, 3]:
    if beat == 1:
        # Dm7: D, F, A, C
        for pitch in [62, 65, 67, 64]:
            note = pretty_midi.Note(velocity=100, pitch=pitch, start=beat * BEAT + 2 * BAR, end=beat * BEAT + 2 * BAR + 0.25 * BEAT)
            piano.notes.append(note)
    elif beat == 3:
        # F7: F, A, C, E
        for pitch in [65, 68, 72, 74]:
            note = pretty_midi.Note(velocity=100, pitch=pitch, start=beat * BEAT + 2 * BAR, end=beat * BEAT + 2 * BAR + 0.25 * BEAT)
            piano.notes.append(note)

# Save the MIDI file
midi.write("dante_russo_intro.mid")
