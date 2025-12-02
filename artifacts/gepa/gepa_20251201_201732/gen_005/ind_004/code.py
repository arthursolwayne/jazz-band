
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
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
        note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking bass line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: D2, F, D, E
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.75),
    pretty_midi.Note(velocity=100, pitch=40, start=1.75, end=2.0),
    pretty_midi.Note(velocity=100, pitch=38, start=2.0, end=2.25),
    pretty_midi.Note(velocity=100, pitch=41, start=2.25, end=2.5),
    # Bar 3: G2, A, G, Bb
    pretty_midi.Note(velocity=100, pitch=43, start=2.5, end=2.75),
    pretty_midi.Note(velocity=100, pitch=45, start=2.75, end=3.0),
    pretty_midi.Note(velocity=100, pitch=43, start=3.0, end=3.25),
    pretty_midi.Note(velocity=100, pitch=42, start=3.25, end=3.5),
    # Bar 4: D2, F, D, E
    pretty_midi.Note(velocity=100, pitch=38, start=3.5, end=3.75),
    pretty_midi.Note(velocity=100, pitch=40, start=3.75, end=4.0),
    pretty_midi.Note(velocity=100, pitch=38, start=4.0, end=4.25),
    pretty_midi.Note(velocity=100, pitch=41, start=4.25, end=4.5),
]
bass.notes.extend(bass_notes)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (F, A, D, G)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=40, start=1.5, end=2.0),
    pretty_midi.Note(velocity=100, pitch=45, start=1.5, end=2.0),
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=2.0),
    pretty_midi.Note(velocity=100, pitch=55, start=1.5, end=2.0),
]
# Bar 3: G7 (B, D, G, B)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=46, start=2.5, end=3.0),
    pretty_midi.Note(velocity=100, pitch=49, start=2.5, end=3.0),
    pretty_midi.Note(velocity=100, pitch=53, start=2.5, end=3.0),
    pretty_midi.Note(velocity=100, pitch=58, start=2.5, end=3.0),
])
# Bar 4: Dm7 (F, A, D, G)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=40, start=3.5, end=4.0),
    pretty_midi.Note(velocity=100, pitch=45, start=3.5, end=4.0),
    pretty_midi.Note(velocity=100, pitch=50, start=3.5, end=4.0),
    pretty_midi.Note(velocity=100, pitch=55, start=3.5, end=4.0),
])
piano.notes.extend(piano_notes)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 4):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)

# Dante: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: Dm (D, F, G, E)
# Bar 2: Start motif on beat 1
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=50, start=1.5, end=1.75),
    pretty_midi.Note(velocity=110, pitch=53, start=1.75, end=2.0),
    pretty_midi.Note(velocity=110, pitch=55, start=2.0, end=2.25),
    pretty_midi.Note(velocity=110, pitch=52, start=2.25, end=2.5),
    # Leave it hanging on beat 3
    pretty_midi.Note(velocity=110, pitch=55, start=2.5, end=2.75),
    # Come back and finish it on beat 4
    pretty_midi.Note(velocity=110, pitch=50, start=2.75, end=3.0),
    # Repeat the motif
    pretty_midi.Note(velocity=110, pitch=50, start=3.0, end=3.25),
    pretty_midi.Note(velocity=110, pitch=53, start=3.25, end=3.5),
    pretty_midi.Note(velocity=110, pitch=55, start=3.5, end=3.75),
    pretty_midi.Note(velocity=110, pitch=52, start=3.75, end=4.0),
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write('dante_intro.mid')
