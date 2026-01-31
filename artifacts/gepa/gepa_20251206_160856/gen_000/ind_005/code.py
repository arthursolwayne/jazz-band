
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
    # Hi-hat on every eighth
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

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line with chromatic approaches
bass_notes = [
    # Bar 2 (1.5s)
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=39, start=1.875, end=2.25), # F#
    pretty_midi.Note(velocity=90, pitch=38, start=2.25, end=2.625), # F
    pretty_midi.Note(velocity=90, pitch=37, start=2.625, end=3.0),  # E
    # Bar 3 (3.0s)
    pretty_midi.Note(velocity=90, pitch=36, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=90, pitch=38, start=3.375, end=3.75), # F
    pretty_midi.Note(velocity=90, pitch=37, start=3.75, end=4.125), # E
    pretty_midi.Note(velocity=90, pitch=36, start=4.125, end=4.5),  # D
    # Bar 4 (4.5s)
    pretty_midi.Note(velocity=90, pitch=38, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=90, pitch=39, start=4.875, end=5.25), # F#
    pretty_midi.Note(velocity=90, pitch=38, start=5.25, end=5.625), # F
    pretty_midi.Note(velocity=90, pitch=37, start=5.625, end=6.0),  # E
]
bass.notes.extend(bass_notes)

# Piano: open voicings, different chord each bar
# Bar 2: Fm7 (F, Ab, C, Eb)
piano_notes = [
    pretty_midi.Note(velocity=95, pitch=53, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=95, pitch=51, start=1.5, end=1.875),  # Ab
    pretty_midi.Note(velocity=95, pitch=57, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=95, pitch=50, start=1.5, end=1.875),  # Eb
]
# Bar 3: Bb7 (Bb, D, F, Ab)
piano_notes.extend([
    pretty_midi.Note(velocity=95, pitch=51, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=95, pitch=55, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=95, pitch=53, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=95, pitch=51, start=3.0, end=3.375),  # Ab
])
# Bar 4: Gm7 (G, Bb, D, F)
piano_notes.extend([
    pretty_midi.Note(velocity=95, pitch=55, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=95, pitch=51, start=4.5, end=4.875),  # Bb
    pretty_midi.Note(velocity=95, pitch=58, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=95, pitch=53, start=4.5, end=4.875),  # F
])
piano.notes.extend(piano_notes)

# Sax: short motif with a question. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: Start the motif
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),  # Bb
    pretty_midi.Note(velocity=110, pitch=66, start=1.875, end=2.25), # D
    pretty_midi.Note(velocity=110, pitch=62, start=2.25, end=2.625), # Bb
    # Bar 3: Leave it hanging
    pretty_midi.Note(velocity=110, pitch=66, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=110, pitch=64, start=3.375, end=3.75), # C
    # Bar 4: Come back and finish it
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.875),  # Bb
    pretty_midi.Note(velocity=110, pitch=66, start=4.875, end=5.25), # D
    pretty_midi.Note(velocity=110, pitch=62, start=5.25, end=5.625), # Bb
    pretty_midi.Note(velocity=110, pitch=64, start=5.625, end=6.0),  # C
]
sax.notes.extend(sax_notes)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save MIDI file
# midi.write disabled
