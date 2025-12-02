
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
for beat in range(4):
    time = beat * 0.375
    if beat % 2 == 0:
        note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
        drums.notes.append(note)
    else:
        note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
        drums.notes.append(note)
    note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125)
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line, chromatic approaches, never the same note twice
# F minor walking bass line: F, Gb, G, Ab, A, Bb, B, C, etc.
bass_notes = [77, 76, 78, 77, 79, 78, 80, 79, 81, 80, 82, 81, 83, 82, 84, 83]
for i, note in enumerate(bass_notes):
    time = 1.5 + (i * 0.375)
    bass_note = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.125)
    bass.notes.append(bass_note)

# Diane: 7th chords, comp on 2 and 4
# F7 = F, A, C, Eb
# Bb7 = Bb, D, F, Ab
# Progression: F7 - Bb7 - F7 - Bb7
chords = [
    [77, 82, 79, 76],  # F7
    [74, 79, 77, 75],  # Bb7
    [77, 82, 79, 76],  # F7
    [74, 79, 77, 75]   # Bb7
]
for bar in range(2, 5):
    for i, chord in enumerate(chords):
        time = 1.5 + ((bar - 2) * 1.5) + (i * 0.75)
        for note in chord:
            piano_note = pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.25)
            piano.notes.append(piano_note)

# You: Tenor sax, one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F (77), G (78), Bb (77), F (77) - but with a twist
# First phrase: F, G, Bb, F (bar 2, beats 1-2)
# Second phrase: G, A, C, F (bar 3, beats 1-2)
# Then resolution: F, Ab, Bb, F (bar 4, beats 1-2)
sax_notes = [
    # Bar 2
    [77, 78, 76, 77],
    # Bar 3
    [78, 79, 81, 77],
    # Bar 4
    [77, 75, 76, 77]
]
for i, phrase in enumerate(sax_notes):
    for j, note in enumerate(phrase):
        time = 1.5 + (i * 1.5) + (j * 0.375)
        sax_note = pretty_midi.Note(velocity=105, pitch=note, start=time, end=time + 0.125)
        sax.notes.append(sax_note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
