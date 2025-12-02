
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
        if beat in [0, 2]:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
        if beat in [1, 3]:
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: D2 (38)
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.625),
    # Bar 2: F2 (41) - chromatic approach
    pretty_midi.Note(velocity=100, pitch=41, start=1.625, end=1.75),
    # Bar 2: G2 (43)
    pretty_midi.Note(velocity=100, pitch=43, start=1.75, end=1.875),
    # Bar 2: A2 (45)
    pretty_midi.Note(velocity=100, pitch=45, start=1.875, end=2.0),

    # Bar 3: C3 (48)
    pretty_midi.Note(velocity=100, pitch=48, start=2.0, end=2.125),
    # Bar 3: D3 (49) - chromatic approach
    pretty_midi.Note(velocity=100, pitch=49, start=2.125, end=2.25),
    # Bar 3: E3 (50)
    pretty_midi.Note(velocity=100, pitch=50, start=2.25, end=2.375),
    # Bar 3: F3 (52)
    pretty_midi.Note(velocity=100, pitch=52, start=2.375, end=2.5),

    # Bar 4: A2 (45)
    pretty_midi.Note(velocity=100, pitch=45, start=2.5, end=2.625),
    # Bar 4: B2 (47) - chromatic approach
    pretty_midi.Note(velocity=100, pitch=47, start=2.625, end=2.75),
    # Bar 4: C3 (48)
    pretty_midi.Note(velocity=100, pitch=48, start=2.75, end=2.875),
    # Bar 4: D3 (49)
    pretty_midi.Note(velocity=100, pitch=49, start=2.875, end=3.0)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: C7 (F7) - C, E, G, Bb, D
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.75),
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.75),
    pretty_midi.Note(velocity=100, pitch=78, start=1.5, end=1.75),
    pretty_midi.Note(velocity=100, pitch=79, start=1.5, end=1.75),
    pretty_midi.Note(velocity=100, pitch=82, start=1.5, end=1.75),

    # Bar 3: B7 (Gm7) - B, D, F, A
    pretty_midi.Note(velocity=100, pitch=71, start=2.0, end=2.25),
    pretty_midi.Note(velocity=100, pitch=74, start=2.0, end=2.25),
    pretty_midi.Note(velocity=100, pitch=76, start=2.0, end=2.25),
    pretty_midi.Note(velocity=100, pitch=77, start=2.0, end=2.25),

    # Bar 4: E7 (Cm7) - E, G, Bb, D
    pretty_midi.Note(velocity=100, pitch=64, start=2.5, end=2.75),
    pretty_midi.Note(velocity=100, pitch=67, start=2.5, end=2.75),
    pretty_midi.Note(velocity=100, pitch=69, start=2.5, end=2.75),
    pretty_midi.Note(velocity=100, pitch=71, start=2.5, end=2.75),
    pretty_midi.Note(velocity=100, pitch=74, start=2.5, end=2.75)
]
piano.notes.extend(piano_notes)

# Drums: continue kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 4):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat in [0, 2]:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
        if beat in [1, 3]:
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: Start of motif
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.625),
    pretty_midi.Note(velocity=110, pitch=65, start=1.625, end=1.75),
    pretty_midi.Note(velocity=110, pitch=67, start=1.75, end=1.875),

    # Bar 3: Leave it hanging
    pretty_midi.Note(velocity=110, pitch=65, start=2.0, end=2.125),
    pretty_midi.Note(velocity=110, pitch=62, start=2.125, end=2.25),

    # Bar 4: Come back and finish it
    pretty_midi.Note(velocity=110, pitch=67, start=2.5, end=2.625),
    pretty_midi.Note(velocity=110, pitch=69, start=2.625, end=2.75)
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_russo_intro.mid")
