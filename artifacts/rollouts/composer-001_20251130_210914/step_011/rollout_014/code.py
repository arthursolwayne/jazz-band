
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
        # Hi-hat on every eighth
        note = pretty_midi.Note(velocity=90, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line - walking line with chromatic approaches
bass_notes = [
    (pretty_midi.Note(velocity=90, pitch=45, start=1.5, end=1.625)),  # F
    (pretty_midi.Note(velocity=90, pitch=46, start=1.625, end=1.75)), # F#
    (pretty_midi.Note(velocity=90, pitch=47, start=1.75, end=1.875)), # G
    (pretty_midi.Note(velocity=90, pitch=49, start=1.875, end=2.0)),  # A
    (pretty_midi.Note(velocity=90, pitch=50, start=2.0, end=2.125)),  # A#
    (pretty_midi.Note(velocity=90, pitch=51, start=2.125, end=2.25)), # B
    (pretty_midi.Note(velocity=90, pitch=53, start=2.25, end=2.375)), # C
    (pretty_midi.Note(velocity=90, pitch=54, start=2.375, end=2.5)),  # C#
    (pretty_midi.Note(velocity=90, pitch=55, start=2.5, end=2.625)),  # D
    (pretty_midi.Note(velocity=90, pitch=57, start=2.625, end=2.75)), # E
    (pretty_midi.Note(velocity=90, pitch=58, start=2.75, end=2.875)), # F
    (pretty_midi.Note(velocity=90, pitch=59, start=2.875, end=3.0)),  # F#
    (pretty_midi.Note(velocity=90, pitch=60, start=3.0, end=3.125)),  # G
    (pretty_midi.Note(velocity=90, pitch=62, start=3.125, end=3.25)), # A
    (pretty_midi.Note(velocity=90, pitch=63, start=3.25, end=3.375)), # A#
    (pretty_midi.Note(velocity=90, pitch=64, start=3.375, end=3.5)),  # B
    (pretty_midi.Note(velocity=90, pitch=66, start=3.5, end=3.625)),  # C
    (pretty_midi.Note(velocity=90, pitch=67, start=3.625, end=3.75)), # C#
    (pretty_midi.Note(velocity=90, pitch=68, start=3.75, end=3.875)), # D
    (pretty_midi.Note(velocity=90, pitch=70, start=3.875, end=4.0)),  # E
    (pretty_midi.Note(velocity=90, pitch=71, start=4.0, end=4.125)),  # F
    (pretty_midi.Note(velocity=90, pitch=72, start=4.125, end=4.25)), # F#
    (pretty_midi.Note(velocity=90, pitch=73, start=4.25, end=4.375)), # G
    (pretty_midi.Note(velocity=90, pitch=75, start=4.375, end=4.5)),  # A
    (pretty_midi.Note(velocity=90, pitch=76, start=4.5, end=4.625)),  # A#
    (pretty_midi.Note(velocity=90, pitch=77, start=4.625, end=4.75)), # B
    (pretty_midi.Note(velocity=90, pitch=79, start=4.75, end=5.0)),   # C
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),   # F7 - F
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=1.75),   # F7 - Bb
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.75),   # F7 - C
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.75),   # F7 - E
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),   # F7 - F
    pretty_midi.Note(velocity=100, pitch=66, start=3.0, end=3.25),   # F7 - Bb
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.25),   # F7 - C
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.25),   # F7 - E
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),   # F7 - F
    pretty_midi.Note(velocity=100, pitch=66, start=4.5, end=4.75),   # F7 - Bb
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.75),   # F7 - C
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.75),   # F7 - E
]
piano.notes.extend(piano_notes)

# Sax: Short motif, start it, leave it hanging, come back and finish it

# Bar 2 - start the motif
note = pretty_midi.Note(velocity=110, pitch=66, start=1.5, end=1.75)   # A
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=69, start=1.75, end=2.0)   # C
sax.notes.append(note)

# Bar 3 - leave it hanging
note = pretty_midi.Note(velocity=110, pitch=69, start=3.0, end=3.125)  # C
sax.notes.append(note)

# Bar 4 - finish it
note = pretty_midi.Note(velocity=110, pitch=71, start=4.5, end=4.75)   # E
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=69, start=4.75, end=5.0)   # C
sax.notes.append(note)

# Drums: Bar 2-4
for bar in range(2, 4):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        # Hi-hat on every eighth
        note = pretty_midi.Note(velocity=90, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write('dante_intro.mid')
