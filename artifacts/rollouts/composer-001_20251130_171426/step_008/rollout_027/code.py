
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
        if beat % 2 == 0:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
        else:
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line, chromatic approaches, no repeated notes
# Dm7: D, F, A, C
# Walking bass line: D -> C -> B -> A -> G -> F -> E -> D -> C -> B -> A -> G -> F -> E -> D
bass_notes = [62, 60, 59, 57, 55, 53, 52, 62, 60, 59, 57, 55, 53, 52, 62]
for i, note in enumerate(bass_notes):
    time = 1.5 + i * 0.375
    note_obj = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.375)
    bass.notes.append(note_obj)

# Diane: 7th chords on 2 and 4
# Dm7: D, F, A, C
# D7: D, F, A, C#
# Gm7: G, Bb, D, F
# Cm7: C, Eb, G, Bb
piano_notes = []
bar = 0
for bar in range(2, 5):
    time = bar * 1.5
    if bar % 2 == 0:
        # Dm7 on 1
        for pitch in [62, 64, 67, 60]:
            piano_notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.375))
    # D7 on 2
    if bar % 2 == 1:
        for pitch in [62, 64, 67, 61]:
            piano_notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=time + 0.75, end=time + 1.125))
    # Gm7 on 3
    for pitch in [67, 69, 71, 67]:
        piano_notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=time + 1.125, end=time + 1.5))
    # Cm7 on 4
    for pitch in [60, 62, 67, 64]:
        piano_notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=time + 1.5, end=time + 1.875))
piano.notes.extend(piano_notes)

# You: Tenor sax. One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Dm scale: D, Eb, F, G, A, Bb, C, D
# Motif: D -> Eb -> F -> A (hanging on A), then back to D
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.625),
    pretty_midi.Note(velocity=110, pitch=63, start=1.625, end=1.75),
    pretty_midi.Note(velocity=110, pitch=64, start=1.75, end=1.875),
    pretty_midi.Note(velocity=110, pitch=67, start=1.875, end=2.0),
    pretty_midi.Note(velocity=110, pitch=62, start=2.375, end=2.5),
    pretty_midi.Note(velocity=110, pitch=63, start=2.5, end=2.625),
    pretty_midi.Note(velocity=110, pitch=64, start=2.625, end=2.75),
    pretty_midi.Note(velocity=110, pitch=67, start=2.75, end=2.875)
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
