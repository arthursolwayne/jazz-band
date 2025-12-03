
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
        note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line in Dm, roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2 (D2, F2, D2, E2)
    pretty_midi.Note(velocity=90, pitch=37, start=1.5, end=1.5 + 0.375),
    pretty_midi.Note(velocity=90, pitch=39, start=1.875, end=1.875 + 0.375),
    pretty_midi.Note(velocity=90, pitch=37, start=2.25, end=2.25 + 0.375),
    pretty_midi.Note(velocity=90, pitch=40, start=2.625, end=2.625 + 0.375),
    # Bar 3 (F2, D2, E2, F2)
    pretty_midi.Note(velocity=90, pitch=39, start=3.0, end=3.0 + 0.375),
    pretty_midi.Note(velocity=90, pitch=37, start=3.375, end=3.375 + 0.375),
    pretty_midi.Note(velocity=90, pitch=40, start=3.75, end=3.75 + 0.375),
    pretty_midi.Note(velocity=90, pitch=39, start=4.125, end=4.125 + 0.375),
    # Bar 4 (D2, F2, D2, C2)
    pretty_midi.Note(velocity=90, pitch=37, start=4.5, end=4.5 + 0.375),
    pretty_midi.Note(velocity=90, pitch=39, start=4.875, end=4.875 + 0.375),
    pretty_midi.Note(velocity=90, pitch=37, start=5.25, end=5.25 + 0.375),
    pretty_midi.Note(velocity=90, pitch=36, start=5.625, end=5.625 + 0.375),
]
bass.notes.extend(bass_notes)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (F, A, D, G)
diane_notes = [
    pretty_midi.Note(velocity=100, pitch=40, start=1.5, end=1.5 + 0.375),
    pretty_midi.Note(velocity=100, pitch=43, start=1.5, end=1.5 + 0.375),
    pretty_midi.Note(velocity=100, pitch=45, start=1.5, end=1.5 + 0.375),
    pretty_midi.Note(velocity=100, pitch=47, start=1.5, end=1.5 + 0.375),
    # Bar 3: G7 (B, D, G, F)
    pretty_midi.Note(velocity=100, pitch=46, start=3.0, end=3.0 + 0.375),
    pretty_midi.Note(velocity=100, pitch=48, start=3.0, end=3.0 + 0.375),
    pretty_midi.Note(velocity=100, pitch=50, start=3.0, end=3.0 + 0.375),
    pretty_midi.Note(velocity=100, pitch=44, start=3.0, end=3.0 + 0.375),
    # Bar 4: Cm7 (E, G, C, Bb)
    pretty_midi.Note(velocity=100, pitch=43, start=4.5, end=4.5 + 0.375),
    pretty_midi.Note(velocity=100, pitch=47, start=4.5, end=4.5 + 0.375),
    pretty_midi.Note(velocity=100, pitch=50, start=4.5, end=4.5 + 0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.5 + 0.375),
]
piano.notes.extend(diane_notes)

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
# Melody: Dm7 -> G7 -> Cm7

# Bar 2: Dm7 - D (45), F (40), A (43), C (48) -> play D and F (quick triplet)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=45, start=1.5, end=1.5 + 0.125),
    pretty_midi.Note(velocity=110, pitch=40, start=1.625, end=1.625 + 0.125),
    # Leave it hanging
    pretty_midi.Note(velocity=110, pitch=43, start=1.875, end=1.875 + 0.125),
    pretty_midi.Note(velocity=110, pitch=50, start=2.25, end=2.25 + 0.125),
    pretty_midi.Note(velocity=110, pitch=48, start=2.625, end=2.625 + 0.125),
    pretty_midi.Note(velocity=110, pitch=45, start=3.0, end=3.0 + 0.125),
    pretty_midi.Note(velocity=110, pitch=40, start=3.375, end=3.375 + 0.125),
    pretty_midi.Note(velocity=110, pitch=43, start=3.75, end=3.75 + 0.125),
    pretty_midi.Note(velocity=110, pitch=50, start=4.125, end=4.125 + 0.125),
    pretty_midi.Note(velocity=110, pitch=48, start=4.5, end=4.5 + 0.125),
    pretty_midi.Note(velocity=110, pitch=45, start=4.875, end=4.875 + 0.125),
    pretty_midi.Note(velocity=110, pitch=40, start=5.25, end=5.25 + 0.125),
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
