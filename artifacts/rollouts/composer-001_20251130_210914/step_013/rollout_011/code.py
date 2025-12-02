
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
        if beat in [0, 2]:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
        if beat in [1, 3]:
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        for eighth in range(2):
            note = pretty_midi.Note(velocity=80, pitch=42, start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.0625)
            drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Piano: 7th chords, comp on 2 and 4
for bar in range(2, 5):
    time = (bar - 2) * 1.5
    if bar % 2 == 0:
        # Root position 7th chords
        if bar == 2:
            # D7
            for note in [D, F#, A, C]:
                note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375)
                piano.notes.append(note)
        elif bar == 4:
            # G7
            for note in [G, B, D, F]:
                note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375)
                piano.notes.append(note)
    else:
        # Rootless 7th chords, voicings
        if bar == 3:
            # Cmaj7 (Dm7)
            for note in [C, E, G, B]:
                note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375)
                piano.notes.append(note)

# Bass: Walking line, chromatic approaches, no repeated notes
bass_notes = [D, F#, G, A, B, C, D, E, F, G, A, B, C, D, E, F]
for i, note in enumerate(bass_notes):
    time = i * 0.375
    if time >= 1.5 and time < 6.0:
        note_obj = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.125)
        bass.notes.append(note_obj)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (D, 0.0), (F#, 0.0), (A, 0.0), (D, 0.375),
    (C, 0.75), (B, 1.125), (A, 1.5), (G, 1.875), (F#, 2.25),
    (D, 2.625), (F#, 2.625), (A, 2.625), (D, 3.0)
]

for pitch, start in sax_notes:
    end = start + 0.125
    note = pretty_midi.Note(velocity=110, pitch=pitch, start=start, end=end)
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
