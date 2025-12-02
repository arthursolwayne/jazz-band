
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
bar_length = 1.5
for beat in range(4):
    time = beat * bar_length / 4
    if beat % 2 == 0:
        note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.1)
        drums.notes.append(note)
    else:
        note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.1)
        drums.notes.append(note)
    note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.1)
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus on bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches, not scales
bass_notes = [
    # Bar 2: D2 (38), F2 (40), G2 (43), D2 (38)
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.5 + 0.375),
    pretty_midi.Note(velocity=90, pitch=40, start=1.5 + 0.375, end=1.5 + 0.75),
    pretty_midi.Note(velocity=90, pitch=43, start=1.5 + 0.75, end=1.5 + 1.125),
    pretty_midi.Note(velocity=90, pitch=38, start=1.5 + 1.125, end=1.5 + 1.5),
    
    # Bar 3: G2 (43), A2 (45), Bb2 (46), G2 (43)
    pretty_midi.Note(velocity=90, pitch=43, start=1.5 + 1.5, end=1.5 + 1.875),
    pretty_midi.Note(velocity=90, pitch=45, start=1.5 + 1.875, end=1.5 + 2.25),
    pretty_midi.Note(velocity=90, pitch=46, start=1.5 + 2.25, end=1.5 + 2.625),
    pretty_midi.Note(velocity=90, pitch=43, start=1.5 + 2.625, end=1.5 + 3.0),
    
    # Bar 4: D2 (38), F2 (40), G2 (43), C3 (52)
    pretty_midi.Note(velocity=90, pitch=38, start=1.5 + 3.0, end=1.5 + 3.375),
    pretty_midi.Note(velocity=90, pitch=40, start=1.5 + 3.375, end=1.5 + 3.75),
    pretty_midi.Note(velocity=90, pitch=43, start=1.5 + 3.75, end=1.5 + 4.125),
    pretty_midi.Note(velocity=90, pitch=52, start=1.5 + 4.125, end=1.5 + 4.5),
]
bass.notes.extend(bass_notes)

# Diane on piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D, F, A, C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.5 + 0.375),
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.5 + 0.375),
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.5 + 0.375),
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.5 + 0.375),

    # Bar 3: G7 (G, B, D, F)
    pretty_midi.Note(velocity=100, pitch=67, start=1.5 + 1.5, end=1.5 + 1.875),
    pretty_midi.Note(velocity=100, pitch=71, start=1.5 + 1.5, end=1.5 + 1.875),
    pretty_midi.Note(velocity=100, pitch=69, start=1.5 + 1.5, end=1.5 + 1.875),
    pretty_midi.Note(velocity=100, pitch=64, start=1.5 + 1.5, end=1.5 + 1.875),

    # Bar 4: Cmaj7 (C, E, G, B)
    pretty_midi.Note(velocity=100, pitch=60, start=1.5 + 3.0, end=1.5 + 3.375),
    pretty_midi.Note(velocity=100, pitch=64, start=1.5 + 3.0, end=1.5 + 3.375),
    pretty_midi.Note(velocity=100, pitch=67, start=1.5 + 3.0, end=1.5 + 3.375),
    pretty_midi.Note(velocity=100, pitch=71, start=1.5 + 3.0, end=1.5 + 3.375),
]
piano.notes.extend(piano_notes)

# Little Ray on drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(3):
    start_time = 1.5 + bar * bar_length
    for beat in range(4):
        time = start_time + (beat * bar_length / 4)
        if beat % 2 == 0:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.1)
            drums.notes.append(note)
        else:
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.1)
            drums.notes.append(note)
        note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.1)
        drums.notes.append(note)

# Dante on sax: One short motif, start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: Motif starts
    pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.5 + 0.375),
    pretty_midi.Note(velocity=110, pitch=67, start=1.5 + 0.375, end=1.5 + 0.75),
    pretty_midi.Note(velocity=110, pitch=65, start=1.5 + 0.75, end=1.5 + 1.125),
    
    # Bar 3: Rest
    pretty_midi.Note(velocity=110, pitch=65, start=1.5 + 1.5, end=1.5 + 1.5 + 0.375),
    pretty_midi.Note(velocity=110, pitch=67, start=1.5 + 1.5 + 0.375, end=1.5 + 1.5 + 0.75),
    pretty_midi.Note(velocity=110, pitch=65, start=1.5 + 1.5 + 0.75, end=1.5 + 1.5 + 1.125),
    
    # Bar 4: Finish the motif
    pretty_midi.Note(velocity=110, pitch=65, start=1.5 + 3.0, end=1.5 + 3.0 + 0.375),
    pretty_midi.Note(velocity=110, pitch=67, start=1.5 + 3.0 + 0.375, end=1.5 + 3.0 + 0.75),
    pretty_midi.Note(velocity=110, pitch=65, start=1.5 + 3.0 + 0.75, end=1.5 + 3.0 + 1.125),
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
