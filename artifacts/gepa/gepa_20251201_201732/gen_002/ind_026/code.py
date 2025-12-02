
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
    pretty_midi.Note(velocity=90, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=95, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=95, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet starts here (1.5 - 3.0s)
# Bass: Walking line (F2 - C3), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=77, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=80, pitch=78, start=1.875, end=2.25),  # F#2 (chromatic)
    pretty_midi.Note(velocity=80, pitch=80, start=2.25, end=2.625),  # G2
    pretty_midi.Note(velocity=80, pitch=77, start=2.625, end=3.0),   # F2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2: Fmaj7 (F, A, C, E)
    pretty_midi.Note(velocity=100, pitch=77, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=82, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=84, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=87, start=1.5, end=1.875),
    # Bar 3: Bbmaj7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=76, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=77, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=80, start=2.25, end=2.625),
    # Bar 4: Dmin7 (D, F, A, C)
    pretty_midi.Note(velocity=100, pitch=74, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=77, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=79, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=84, start=2.625, end=3.0),
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Start with a smooth F to Bb to D (F4, Bb4, D5), then resolve on the last bar
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=84, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=110, pitch=87, start=1.875, end=2.25),  # Bb4
    pretty_midi.Note(velocity=110, pitch=90, start=2.25, end=2.625),  # D5
    pretty_midi.Note(velocity=110, pitch=84, start=2.625, end=3.0),   # F4 (resolve)
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
