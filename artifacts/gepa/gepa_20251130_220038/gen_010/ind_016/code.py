
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(1):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        for eighth in range(2):
            note = pretty_midi.Note(velocity=80, pitch=42, start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.0625)
            drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line, chromatic approaches
# Dm7 chord: D F A C
# Walking bass line in Dm: D -> F -> E -> G -> F -> A -> G -> Bb
bass_notes = [50, 53, 52, 55, 53, 57, 55, 58]
for bar in range(2, 5):
    for i, note in enumerate(bass_notes):
        time = bar * 1.5 + i * 0.375
        note_obj = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25)
        bass.notes.append(note_obj)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: Dm7
    (50, 0.0), (53, 0.0), (57, 0.0), (60, 0.0),  # D F A C
    # Bar 3: G7
    (62, 0.0), (65, 0.0), (67, 0.0), (71, 0.0),  # G B D F#
    # Bar 4: Cm7
    (60, 0.0), (63, 0.0), (67, 0.0), (71, 0.0),  # C Eb G Bb
]
for i, (pitch, offset) in enumerate(piano_notes):
    time = (i // 4 + 2) * 1.5 + offset * 0.375
    note_obj = pretty_midi.Note(velocity=95, pitch=pitch, start=time, end=time + 0.25)
    piano.notes.append(note_obj)

# Sax: Motif - D, F#, A, D - played as quarter notes
sax_notes = [50, 57, 57, 50]  # D, F#, A, D
for i, pitch in enumerate(sax_notes):
    time = 2 * 1.5 + i * 0.375
    note_obj = pretty_midi.Note(velocity=105, pitch=pitch, start=time, end=time + 0.25)
    sax.notes.append(note_obj)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save MIDI file
midi.write("dante_intro.mid")
