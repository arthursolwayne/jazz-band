
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

# Bass line: walking line in Fm, chromatic approaches
bass_notes = [
    (pretty_midi.Note(velocity=100, pitch=37, start=1.5, end=1.625)),  # F
    (pretty_midi.Note(velocity=100, pitch=36, start=1.625, end=1.75)), # E
    (pretty_midi.Note(velocity=100, pitch=38, start=1.75, end=1.875)), # G
    (pretty_midi.Note(velocity=100, pitch=39, start=1.875, end=2.0)),  # Ab
    (pretty_midi.Note(velocity=100, pitch=41, start=2.0, end=2.125)),  # Bb
    (pretty_midi.Note(velocity=100, pitch=40, start=2.125, end=2.25)), # A
    (pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.375)), # B
    (pretty_midi.Note(velocity=100, pitch=43, start=2.375, end=2.5)),  # C
    (pretty_midi.Note(velocity=100, pitch=41, start=2.5, end=2.625)),  # Bb
    (pretty_midi.Note(velocity=100, pitch=40, start=2.625, end=2.75)), # A
    (pretty_midi.Note(velocity=100, pitch=38, start=2.75, end=2.875)), # G
    (pretty_midi.Note(velocity=100, pitch=37, start=2.875, end=3.0)),  # F
    (pretty_midi.Note(velocity=100, pitch=35, start=3.0, end=3.125)),  # Eb
    (pretty_midi.Note(velocity=100, pitch=36, start=3.125, end=3.25)), # E
    (pretty_midi.Note(velocity=100, pitch=38, start=3.25, end=3.375)), # G
    (pretty_midi.Note(velocity=100, pitch=39, start=3.375, end=3.5)),  # Ab
    (pretty_midi.Note(velocity=100, pitch=41, start=3.5, end=3.625)),  # Bb
    (pretty_midi.Note(velocity=100, pitch=40, start=3.625, end=3.75)), # A
    (pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=3.875)), # B
    (pretty_midi.Note(velocity=100, pitch=43, start=3.875, end=4.0)),  # C
    (pretty_midi.Note(velocity=100, pitch=41, start=4.0, end=4.125)),  # Bb
    (pretty_midi.Note(velocity=100, pitch=40, start=4.125, end=4.25)), # A
    (pretty_midi.Note(velocity=100, pitch=38, start=4.25, end=4.375)), # G
    (pretty_midi.Note(velocity=100, pitch=37, start=4.375, end=4.5)),  # F
    (pretty_midi.Note(velocity=100, pitch=35, start=4.5, end=4.625)),  # Eb
    (pretty_midi.Note(velocity=100, pitch=36, start=4.625, end=4.75)), # E
    (pretty_midi.Note(velocity=100, pitch=38, start=4.75, end=4.875)), # G
    (pretty_midi.Note(velocity=100, pitch=39, start=4.875, end=5.0)),  # Ab
    (pretty_midi.Note(velocity=100, pitch=41, start=5.0, end=5.125)),  # Bb
    (pretty_midi.Note(velocity=100, pitch=40, start=5.125, end=5.25)), # A
    (pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.375)), # B
    (pretty_midi.Note(velocity=100, pitch=43, start=5.375, end=5.5)),  # C
    (pretty_midi.Note(velocity=100, pitch=41, start=5.5, end=5.625)),  # Bb
    (pretty_midi.Note(velocity=100, pitch=40, start=5.625, end=5.75)), # A
    (pretty_midi.Note(velocity=100, pitch=38, start=5.75, end=5.875)), # G
    (pretty_midi.Note(velocity=100, pitch=37, start=5.875, end=6.0)),  # F
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
# F7 on 2, Bb7 on 4
piano_notes = [
    # Bar 2 (1.5 - 2.0)
    (pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.625)), # F
    (pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.625)), # A
    (pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.625)), # Bb
    (pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.625)), # C
    # Bar 3 (2.0 - 2.5)
    (pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.125)), # Bb
    (pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.125)), # D
    (pretty_midi.Note(velocity=100, pitch=69, start=2.0, end=2.125)), # F
    (pretty_midi.Note(velocity=100, pitch=71, start=2.0, end=2.125)), # G
    # Bar 4 (2.5 - 3.0)
    (pretty_midi.Note(velocity=100, pitch=64, start=2.5, end=2.625)), # F
    (pretty_midi.Note(velocity=100, pitch=69, start=2.5, end=2.625)), # A
    (pretty_midi.Note(velocity=100, pitch=71, start=2.5, end=2.625)), # Bb
    (pretty_midi.Note(velocity=100, pitch=67, start=2.5, end=2.625)), # C
    # Bar 5 (3.0 - 3.5)
    (pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.125)), # Bb
    (pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.125)), # D
    (pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.125)), # F
    (pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.125)), # G
    # Bar 6 (3.5 - 4.0)
    (pretty_midi.Note(velocity=100, pitch=64, start=3.5, end=3.625)), # F
    (pretty_midi.Note(velocity=100, pitch=69, start=3.5, end=3.625)), # A
    (pretty_midi.Note(velocity=100, pitch=71, start=3.5, end=3.625)), # Bb
    (pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=3.625)), # C
    # Bar 7 (4.0 - 4.5)
    (pretty_midi.Note(velocity=100, pitch=62, start=4.0, end=4.125)), # Bb
    (pretty_midi.Note(velocity=100, pitch=67, start=4.0, end=4.125)), # D
    (pretty_midi.Note(velocity=100, pitch=69, start=4.0, end=4.125)), # F
    (pretty_midi.Note(velocity=100, pitch=71, start=4.0, end=4.125)), # G
    # Bar 8 (4.5 - 5.0)
    (pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.625)), # F
    (pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.625)), # A
    (pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.625)), # Bb
    (pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.625)), # C
    # Bar 9 (5.0 - 5.5)
    (pretty_midi.Note(velocity=100, pitch=62, start=5.0, end=5.125)), # Bb
    (pretty_midi.Note(velocity=100, pitch=67, start=5.0, end=5.125)), # D
    (pretty_midi.Note(velocity=100, pitch=69, start=5.0, end=5.125)), # F
    (pretty_midi.Note(velocity=100, pitch=71, start=5.0, end=5.125)), # G
    # Bar 10 (5.5 - 6.0)
    (pretty_midi.Note(velocity=100, pitch=64, start=5.5, end=5.625)), # F
    (pretty_midi.Note(velocity=100, pitch=69, start=5.5, end=5.625)), # A
    (pretty_midi.Note(velocity=100, pitch=71, start=5.5, end=5.625)), # Bb
    (pretty_midi.Note(velocity=100, pitch=67, start=5.5, end=5.625)), # C
]
piano.notes.extend(piano_notes)

# Sax: Melody, one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F, Ab, Bb, F (over 2 bars)
sax_notes = [
    (pretty_midi.Note(velocity=110, pitch=64, start=1.5, end=1.75)),  # F
    (pretty_midi.Note(velocity=110, pitch=67, start=1.75, end=2.0)),   # Ab
    (pretty_midi.Note(velocity=110, pitch=69, start=2.0, end=2.25)),  # Bb
    (pretty_midi.Note(velocity=110, pitch=64, start=2.25, end=2.5)),  # F
    (pretty_midi.Note(velocity=110, pitch=64, start=3.5, end=3.75)),  # F
    (pretty_midi.Note(velocity=110, pitch=67, start=3.75, end=4.0)),   # Ab
    (pretty_midi.Note(velocity=110, pitch=69, start=4.0, end=4.25)),  # Bb
    (pretty_midi.Note(velocity=110, pitch=64, start=4.25, end=4.5)),  # F
    (pretty_midi.Note(velocity=110, pitch=64, start=5.5, end=5.75)),  # F
    (pretty_midi.Note(velocity=110, pitch=67, start=5.75, end=6.0)),   # Ab
]
sax.notes.extend(sax_notes)

# Drums: continue with same pattern
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

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
