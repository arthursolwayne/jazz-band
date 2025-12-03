
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
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line (D2-G2), roots and fifths with chromatic approaches
bass_notes = [
    # D2 (root) on beat 1
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),
    # Eb2 (chromatic approach) on & of 1
    pretty_midi.Note(velocity=90, pitch=39, start=1.875, end=2.0),
    # G2 (fifth) on beat 2
    pretty_midi.Note(velocity=100, pitch=43, start=2.0, end=2.375),
    # A2 (chromatic approach) on & of 2
    pretty_midi.Note(velocity=90, pitch=44, start=2.375, end=2.5625),
    # D2 (root) on beat 3
    pretty_midi.Note(velocity=100, pitch=38, start=2.5625, end=2.9375),
    # Eb2 (chromatic approach) on & of 3
    pretty_midi.Note(velocity=90, pitch=39, start=2.9375, end=3.0),
    # G2 (fifth) on beat 4
    pretty_midi.Note(velocity=100, pitch=43, start=3.0, end=3.375),
    # A2 (chromatic approach) on & of 4
    pretty_midi.Note(velocity=90, pitch=44, start=3.375, end=3.5625)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on last
# Bar 2: Dm7 (D-F-A-C)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=3.0),  # D4
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=3.0),  # F4
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=3.0),  # A4
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=3.0),  # C5
]
piano.notes.extend(piano_notes)

# Sax: Motif - start, leave it hanging, come back and finish
sax_notes = [
    # First note - D4
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75),
    # Leave it hanging
    pretty_midi.Note(velocity=110, pitch=62, start=1.75, end=2.0),
    # Come back and finish it
    pretty_midi.Note(velocity=110, pitch=62, start=2.5, end=2.75),
    pretty_midi.Note(velocity=110, pitch=62, start=2.75, end=3.0)
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line, same pattern as bar 2 but with chromatic approach on F
bass_notes = [
    # F2 (root) on beat 1
    pretty_midi.Note(velocity=100, pitch=41, start=3.0, end=3.375),
    # G2 (chromatic approach) on & of 1
    pretty_midi.Note(velocity=90, pitch=43, start=3.375, end=3.5625),
    # A2 (fifth) on beat 2
    pretty_midi.Note(velocity=100, pitch=44, start=3.5625, end=3.9375),
    # Bb2 (chromatic approach) on & of 2
    pretty_midi.Note(velocity=90, pitch=45, start=3.9375, end=4.125),
    # F2 (root) on beat 3
    pretty_midi.Note(velocity=100, pitch=41, start=4.125, end=4.5),
    # G2 (chromatic approach) on & of 3
    pretty_midi.Note(velocity=90, pitch=43, start=4.5, end=4.6875),
    # A2 (fifth) on beat 4
    pretty_midi.Note(velocity=100, pitch=44, start=4.6875, end=5.0625),
    # Bb2 (chromatic approach) on & of 4
    pretty_midi.Note(velocity=90, pitch=45, start=5.0625, end=5.25)
]
bass.notes.extend(bass_notes)

# Piano: Bar 3: F7 (F-A-C-E)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=65, start=3.0, end=4.5),  # F4
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=4.5),  # A4
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=4.5),  # C5
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=4.5),  # E5
]
piano.notes.extend(piano_notes)

# Sax: Continue motif, add a new phrase
sax_notes = [
    # Continue the motif up a third
    pretty_midi.Note(velocity=110, pitch=67, start=3.0, end=3.25),
    pretty_midi.Note(velocity=110, pitch=67, start=3.25, end=3.5),
    # New phrase
    pretty_midi.Note(velocity=110, pitch=69, start=3.5, end=3.75),
    pretty_midi.Note(velocity=110, pitch=69, start=3.75, end=4.0)
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line, same pattern as bar 2 but with chromatic approach on A
bass_notes = [
    # A2 (root) on beat 1
    pretty_midi.Note(velocity=100, pitch=44, start=4.5, end=4.875),
    # Bb2 (chromatic approach) on & of 1
    pretty_midi.Note(velocity=90, pitch=45, start=4.875, end=5.0625),
    # C3 (fifth) on beat 2
    pretty_midi.Note(velocity=100, pitch=47, start=5.0625, end=5.4375),
    # Db3 (chromatic approach) on & of 2
    pretty_midi.Note(velocity=90, pitch=48, start=5.4375, end=5.625),
    # A2 (root) on beat 3
    pretty_midi.Note(velocity=100, pitch=44, start=5.625, end=6.0),
    # Bb2 (chromatic approach) on & of 3
    pretty_midi.Note(velocity=90, pitch=45, start=6.0, end=6.1875),
    # C3 (fifth) on beat 4
    pretty_midi.Note(velocity=100, pitch=47, start=6.1875, end=6.5625),
    # Db3 (chromatic approach) on & of 4
    pretty_midi.Note(velocity=90, pitch=48, start=6.5625, end=6.75)
]
bass.notes.extend(bass_notes)

# Piano: Bar 4: A7 (A-C#-E-G#)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=6.0),  # A4
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=6.0),  # C#5
    pretty_midi.Note(velocity=90, pitch=74, start=4.5, end=6.0),  # E5
    pretty_midi.Note(velocity=90, pitch=77, start=4.5, end=6.0)   # G#5
]
piano.notes.extend(piano_notes)

# Sax: Finish the motif, resolve it
sax_notes = [
    # Finish the motif
    pretty_midi.Note(velocity=110, pitch=71, start=4.5, end=4.75),
    pretty_midi.Note(velocity=110, pitch=71, start=4.75, end=5.0),
    # Resolve it down a third
    pretty_midi.Note(velocity=110, pitch=67, start=5.0, end=5.25),
    pretty_midi.Note(velocity=110, pitch=67, start=5.25, end=5.5),
    # End on a strong note
    pretty_midi.Note(velocity=110, pitch=62, start=5.5, end=5.75),
    pretty_midi.Note(velocity=110, pitch=62, start=5.75, end=6.0)
]
sax.notes.extend(sax_notes)

# Drums: Bar 3-4 (3.0 - 6.0s)
# Same pattern as Bar 1 repeated
for i in range(2):
    for note in drum_notes:
        new_note = pretty_midi.Note(
            velocity=note.velocity,
            pitch=note.pitch,
            start=note.start + 3.0 * i,
            end=note.end + 3.0 * i
        )
        drums.notes.append(new_note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
