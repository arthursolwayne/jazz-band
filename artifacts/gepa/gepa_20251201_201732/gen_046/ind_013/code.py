
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
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
# Bass: Walking line, roots and fifths with chromatic approaches
bass_notes = [
    # Fm root (F) on beat 1
    pretty_midi.Note(velocity=90, pitch=53, start=1.5, end=1.875),
    # Bb (fifth) with chromatic approach
    pretty_midi.Note(velocity=90, pitch=51, start=1.875, end=2.0),
    pretty_midi.Note(velocity=90, pitch=52, start=2.0, end=2.125),
    pretty_midi.Note(velocity=90, pitch=50, start=2.125, end=2.375),
    # Ab (minor third, chromatic)
    pretty_midi.Note(velocity=90, pitch=49, start=2.375, end=2.625),
    pretty_midi.Note(velocity=90, pitch=47, start=2.625, end=2.875),
    pretty_midi.Note(velocity=90, pitch=48, start=2.875, end=3.0)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7
piano_notes_2 = [
    pretty_midi.Note(velocity=95, pitch=64, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=95, pitch=69, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=95, pitch=67, start=1.5, end=1.875),  # Ab
    pretty_midi.Note(velocity=95, pitch=71, start=1.5, end=1.875),  # D
]
piano.notes.extend(piano_notes_2)

# Bar 3: G7(b9) altered
piano_notes_3 = [
    pretty_midi.Note(velocity=95, pitch=71, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=95, pitch=76, start=3.0, end=3.375),  # B
    pretty_midi.Note(velocity=95, pitch=72, start=3.0, end=3.375),  # Db
    pretty_midi.Note(velocity=95, pitch=74, start=3.0, end=3.375),  # Eb
]
piano.notes.extend(piano_notes_3)

# Bar 4: Cm7
piano_notes_4 = [
    pretty_midi.Note(velocity=95, pitch=60, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=95, pitch=65, start=4.5, end=4.875),  # Eb
    pretty_midi.Note(velocity=95, pitch=63, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=95, pitch=67, start=4.5, end=4.875),  # G
]
piano.notes.extend(piano_notes_4)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Bar 2: Start the motif (F, Ab, Bb, F)
sax_notes_2 = [
    pretty_midi.Note(velocity=110, pitch=53, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=110, pitch=51, start=1.625, end=1.75),  # Ab
    pretty_midi.Note(velocity=110, pitch=52, start=1.75, end=1.875),  # Bb
]
sax.notes.extend(sax_notes_2)

# Bar 4: Return and finish the motif (F, Ab, Bb, F)
sax_notes_4 = [
    pretty_midi.Note(velocity=110, pitch=53, start=4.5, end=4.625),  # F
    pretty_midi.Note(velocity=110, pitch=51, start=4.625, end=4.75),  # Ab
    pretty_midi.Note(velocity=110, pitch=52, start=4.75, end=4.875),  # Bb
    pretty_midi.Note(velocity=110, pitch=53, start=4.875, end=5.0),  # F
]
sax.notes.extend(sax_notes_4)

# Bar 3: Drums and rest
# Kick on 1 and 3
drum_notes_3 = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.3125, end=4.5),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.0)
]
drums.notes.extend(drum_notes_3)

# Bar 3: Full quartet
# Bass: Walking line, roots and fifths with chromatic approaches
bass_notes_3 = [
    # G on beat 1
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.375),
    # C (fifth) with chromatic approach
    pretty_midi.Note(velocity=90, pitch=72, start=3.375, end=3.5),
    pretty_midi.Note(velocity=90, pitch=71, start=3.5, end=3.625),
    pretty_midi.Note(velocity=90, pitch=70, start=3.625, end=3.875),
    # Eb (minor third, chromatic)
    pretty_midi.Note(velocity=90, pitch=67, start=3.875, end=4.125),
    pretty_midi.Note(velocity=90, pitch=65, start=4.125, end=4.375),
    pretty_midi.Note(velocity=90, pitch=66, start=4.375, end=4.5)
]
bass.notes.extend(bass_notes_3)

# Bar 4: Full quartet
# Drums
drum_notes_4 = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.375),
    pretty_midi.Note(velocity=110, pitch=38, start=6.375, end=6.5),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.0625, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=5.4375, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=5.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=5.8125, end=6.0)
]
drums.notes.extend(drum_notes_4)

# Bar 4: Bass
bass_notes_4 = [
    # C on beat 1
    pretty_midi.Note(velocity=90, pitch=60, start=4.5, end=4.875),
    # F (fifth) with chromatic approach
    pretty_midi.Note(velocity=90, pitch=62, start=4.875, end=5.0),
    pretty_midi.Note(velocity=90, pitch=61, start=5.0, end=5.125),
    pretty_midi.Note(velocity=90, pitch=60, start=5.125, end=5.375),
    # Eb (minor third, chromatic)
    pretty_midi.Note(velocity=90, pitch=64, start=5.375, end=5.625),
    pretty_midi.Note(velocity=90, pitch=62, start=5.625, end=5.875),
    pretty_midi.Note(velocity=90, pitch=63, start=5.875, end=6.0)
]
bass.notes.extend(bass_notes_4)

# Bar 4: Piano
# Cm7 resolves on beat 4
piano_notes_4 = [
    pretty_midi.Note(velocity=95, pitch=60, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=95, pitch=65, start=4.5, end=4.875),  # Eb
    pretty_midi.Note(velocity=95, pitch=63, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=95, pitch=67, start=4.5, end=4.875),  # G
]
piano.notes.extend(piano_notes_4)

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
