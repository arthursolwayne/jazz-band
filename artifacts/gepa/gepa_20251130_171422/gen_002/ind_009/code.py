
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Drums only
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

# Bar 2: Everyone in
# Bass: Walking line, Dm7 -> G7 -> Cmaj7 -> F7
# D -> Eb -> F -> G -> A -> Bb -> B -> C
# Dm7: D, F, A, C
# G7: G, Bb, D, F
# Cmaj7: C, E, G, B
# F7: F, A, C, Eb
bass_notes = [50, 53, 55, 57, 59, 60, 62, 64]
for i, note in enumerate(bass_notes):
    time = 1.5 + (i * 0.375)
    note_obj = pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(note_obj)

# Piano: 7th chords, comp on 2 and 4
# Dm7: D, F, A, C
# G7: G, Bb, D, F
# Cmaj7: C, E, G, B
# F7: F, A, C, Eb
piano_notes = [
    # Bar 2 (Dm7)
    (50, 52, 57, 60),
    # Bar 3 (G7)
    (67, 69, 71, 73),
    # Bar 4 (Cmaj7)
    (60, 64, 67, 71),
    # Bar 4 (F7)
    (55, 58, 60, 62)
]
for i, chord in enumerate(piano_notes):
    for note in chord:
        time = 1.5 + (i * 0.375)
        note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25)
        piano.notes.append(note_obj)

# Sax: Melody
# Motif: D -> Eb -> F -> G
# D (50), Eb (51), F (53), G (55)
# Start on D, leave it hanging on Eb, come back on F, end on G
sax_notes = [
    # Bar 2
    pretty_midi.Note(velocity=110, pitch=50, start=1.5, end=1.5 + 0.1875),
    pretty_midi.Note(velocity=110, pitch=51, start=1.5 + 0.375, end=1.5 + 0.5625),
    pretty_midi.Note(velocity=110, pitch=53, start=1.5 + 0.75, end=1.5 + 0.9375),
    pretty_midi.Note(velocity=110, pitch=55, start=1.5 + 1.125, end=1.5 + 1.3125)
]
for note in sax_notes:
    sax.notes.append(note)

# Add instruments to MIDI
midi.instruments = [sax, bass, piano, drums]

# Save MIDI
midi.write("dante_intro.mid")
