
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
        # Hihat on every eighth note
        note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus on bass: Walking line in Fm (F - Ab - D - C), roots and fifths with chromatic approaches
for bar in range(2, 5):
    bar_time = (bar - 1) * 1.5
    if bar == 2:
        # Fm7 (F, Ab, C, D)
        # Bass line: F -> Ab -> D -> C
        notes = [pretty_midi.Note(velocity=90, pitch=71, start=bar_time + 0.0, end=bar_time + 0.375),  # F
                 pretty_midi.Note(velocity=90, pitch=68, start=bar_time + 0.375, end=bar_time + 0.75),  # Ab
                 pretty_midi.Note(velocity=90, pitch=73, start=bar_time + 0.75, end=bar_time + 1.125),  # D
                 pretty_midi.Note(velocity=90, pitch=72, start=bar_time + 1.125, end=bar_time + 1.5)]  # C
    elif bar == 3:
        # Ab7 (Ab, C, Eb, G)
        # Bass line: Ab -> C -> G -> Eb
        notes = [pretty_midi.Note(velocity=90, pitch=68, start=bar_time + 0.0, end=bar_time + 0.375),  # Ab
                 pretty_midi.Note(velocity=90, pitch=72, start=bar_time + 0.375, end=bar_time + 0.75),  # C
                 pretty_midi.Note(velocity=90, pitch=76, start=bar_time + 0.75, end=bar_time + 1.125),  # G
                 pretty_midi.Note(velocity=90, pitch=69, start=bar_time + 1.125, end=bar_time + 1.5)]  # Eb
    elif bar == 4:
        # D7 (D, F#, A, C)
        # Bass line: D -> F# -> C -> A
        notes = [pretty_midi.Note(velocity=90, pitch=73, start=bar_time + 0.0, end=bar_time + 0.375),  # D
                 pretty_midi.Note(velocity=90, pitch=76, start=bar_time + 0.375, end=bar_time + 0.75),  # F#
                 pretty_midi.Note(velocity=90, pitch=72, start=bar_time + 0.75, end=bar_time + 1.125),  # C
                 pretty_midi.Note(velocity=90, pitch=71, start=bar_time + 1.125, end=bar_time + 1.5)]  # A
    bass.notes.extend(notes)

# Diane on piano: Open voicings, different chord each bar, resolve on the last
for bar in range(2, 5):
    bar_time = (bar - 1) * 1.5
    if bar == 2:
        # Fm7: F, Ab, C, D
        notes = [
            pretty_midi.Note(velocity=100, pitch=71, start=bar_time + 0.0, end=bar_time + 0.375),  # F
            pretty_midi.Note(velocity=100, pitch=68, start=bar_time + 0.0, end=bar_time + 0.375),  # Ab
            pretty_midi.Note(velocity=100, pitch=72, start=bar_time + 0.0, end=bar_time + 0.375),  # C
            pretty_midi.Note(velocity=100, pitch=73, start=bar_time + 0.0, end=bar_time + 0.375)   # D
        ]
    elif bar == 3:
        # Ab7: Ab, C, Eb, G
        notes = [
            pretty_midi.Note(velocity=100, pitch=68, start=bar_time + 0.5, end=bar_time + 0.875),  # Ab
            pretty_midi.Note(velocity=100, pitch=72, start=bar_time + 0.5, end=bar_time + 0.875),  # C
            pretty_midi.Note(velocity=100, pitch=69, start=bar_time + 0.5, end=bar_time + 0.875),  # Eb
            pretty_midi.Note(velocity=100, pitch=76, start=bar_time + 0.5, end=bar_time + 0.875)   # G
        ]
    elif bar == 4:
        # D7: D, F#, A, C
        notes = [
            pretty_midi.Note(velocity=100, pitch=73, start=bar_time + 0.5, end=bar_time + 0.875),  # D
            pretty_midi.Note(velocity=100, pitch=76, start=bar_time + 0.5, end=bar_time + 0.875),  # F#
            pretty_midi.Note(velocity=100, pitch=71, start=bar_time + 0.5, end=bar_time + 0.875),  # A
            pretty_midi.Note(velocity=100, pitch=72, start=bar_time + 0.5, end=bar_time + 0.875)   # C
        ]
    piano.notes.extend(notes)

# Little Ray on drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_time = (bar - 1) * 1.5
    for beat in range(4):
        time = bar_time + beat * 0.375
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        # Hihat on every eighth note
        note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)

# Dante on sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F, Ab, D, C (Fm7) -> F, Bb, D, C (F7) -> F, Ab, D, C (Fm7)
# Bar 2: Start motif (F, Ab, D, C)
# Bar 3: Continue motif (F, Bb, D, C)
# Bar 4: Resolve (F, Ab, D, C)

for bar in range(2, 5):
    bar_time = (bar - 1) * 1.5
    if bar == 2:
        # F, Ab, D, C
        notes = [
            pretty_midi.Note(velocity=100, pitch=66, start=bar_time + 0.0, end=bar_time + 0.375),  # F
            pretty_midi.Note(velocity=100, pitch=63, start=bar_time + 0.375, end=bar_time + 0.75),  # Ab
            pretty_midi.Note(velocity=100, pitch=68, start=bar_time + 0.75, end=bar_time + 1.125),  # D
            pretty_midi.Note(velocity=100, pitch=67, start=bar_time + 1.125, end=bar_time + 1.5)   # C
        ]
    elif bar == 3:
        # F, Bb, D, C
        notes = [
            pretty_midi.Note(velocity=100, pitch=66, start=bar_time + 0.0, end=bar_time + 0.375),  # F
            pretty_midi.Note(velocity=100, pitch=62, start=bar_time + 0.375, end=bar_time + 0.75),  # Bb
            pretty_midi.Note(velocity=100, pitch=68, start=bar_time + 0.75, end=bar_time + 1.125),  # D
            pretty_midi.Note(velocity=100, pitch=67, start=bar_time + 1.125, end=bar_time + 1.5)   # C
        ]
    elif bar == 4:
        # F, Ab, D, C (resolve)
        notes = [
            pretty_midi.Note(velocity=100, pitch=66, start=bar_time + 0.0, end=bar_time + 0.375),  # F
            pretty_midi.Note(velocity=100, pitch=63, start=bar_time + 0.375, end=bar_time + 0.75),  # Ab
            pretty_midi.Note(velocity=100, pitch=68, start=bar_time + 0.75, end=bar_time + 1.125),  # D
            pretty_midi.Note(velocity=100, pitch=67, start=bar_time + 1.125, end=bar_time + 1.5)   # C
        ]
    sax.notes.extend(notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
