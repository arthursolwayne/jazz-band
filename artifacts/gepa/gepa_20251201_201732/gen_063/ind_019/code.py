
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
    # Kick on 1 and 3 (0.0, 1.125)
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.3125),
    # Snare on 2 and 4 (0.75, 1.875)
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth (0.0, 0.375, 0.75, 1.125, 1.5, 1.875, 2.25, 2.625)
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=2.8125),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line (F to Bb to Bb to Eb), roots and fifths with chromatic approaches
# Bar 2 (1.5 - 3.0s)
bass_notes = [
    pretty_midi.Note(velocity=70, pitch=43, start=1.5, end=1.75),  # F (root)
    pretty_midi.Note(velocity=70, pitch=42, start=1.75, end=2.0),  # F (chromatic approach)
    pretty_midi.Note(velocity=70, pitch=47, start=2.0, end=2.25),  # Bb (fifth)
    pretty_midi.Note(velocity=70, pitch=46, start=2.25, end=2.5),  # Bb (chromatic approach)
]
# Bar 3 (3.0 - 4.5s)
bass_notes.extend([
    pretty_midi.Note(velocity=70, pitch=46, start=3.0, end=3.25),  # Bb (root)
    pretty_midi.Note(velocity=70, pitch=45, start=3.25, end=3.5),  # Bb (chromatic approach)
    pretty_midi.Note(velocity=70, pitch=50, start=3.5, end=3.75),  # Eb (fifth)
    pretty_midi.Note(velocity=70, pitch=49, start=3.75, end=4.0),  # Eb (chromatic approach)
])
# Bar 4 (4.5 - 6.0s)
bass_notes.extend([
    pretty_midi.Note(velocity=70, pitch=49, start=4.5, end=4.75),  # Eb (root)
    pretty_midi.Note(velocity=70, pitch=48, start=4.75, end=5.0),  # Eb (chromatic approach)
    pretty_midi.Note(velocity=70, pitch=53, start=5.0, end=5.25),  # Ab (fifth)
    pretty_midi.Note(velocity=70, pitch=52, start=5.25, end=5.5),  # Ab (chromatic approach)
])
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2 (1.5 - 3.0s): Fmaj7
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=53, start=1.5, end=3.0),  # F
    pretty_midi.Note(velocity=80, pitch=57, start=1.5, end=3.0),  # A
    pretty_midi.Note(velocity=80, pitch=60, start=1.5, end=3.0),  # C
    pretty_midi.Note(velocity=80, pitch=64, start=1.5, end=3.0),  # E
]
# Bar 3 (3.0 - 4.5s): Bb7
piano_notes.extend([
    pretty_midi.Note(velocity=80, pitch=47, start=3.0, end=4.5),  # Bb
    pretty_midi.Note(velocity=80, pitch=51, start=3.0, end=4.5),  # D
    pretty_midi.Note(velocity=80, pitch=53, start=3.0, end=4.5),  # F
    pretty_midi.Note(velocity=80, pitch=57, start=3.0, end=4.5),  # A
])
# Bar 4 (4.5 - 6.0s): Eb7
piano_notes.extend([
    pretty_midi.Note(velocity=80, pitch=49, start=4.5, end=6.0),  # Eb
    pretty_midi.Note(velocity=80, pitch=53, start=4.5, end=6.0),  # G
    pretty_midi.Note(velocity=80, pitch=55, start=4.5, end=6.0),  # Bb
    pretty_midi.Note(velocity=80, pitch=58, start=4.5, end=6.0),  # D
])
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F (D2) - Bb (E2) - F (D2) (Bar 2)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=57, start=1.875, end=2.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=53, start=2.25, end=2.5),  # F
    # Bar 3: Let it hang, then come back with the motif (Bar 4)
    pretty_midi.Note(velocity=100, pitch=53, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=57, start=4.875, end=5.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=53, start=5.25, end=5.5),  # F
]
sax.notes.extend(sax_notes)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save MIDI file
# midi.write disabled
