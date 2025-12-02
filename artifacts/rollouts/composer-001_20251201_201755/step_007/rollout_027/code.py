
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

# Bar 2: Full quartet (1.5 - 3.0s)
# Marcus: Walking bass line in Fm (F2, Ab2, D2, G2, etc.)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=53, start=1.5, end=1.875), # F2
    pretty_midi.Note(velocity=90, pitch=50, start=1.875, end=2.25), # Ab2
    pretty_midi.Note(velocity=90, pitch=51, start=2.25, end=2.625), # D2
    pretty_midi.Note(velocity=90, pitch=53, start=2.625, end=3.0), # F2
]
bass.notes.extend(bass_notes)

# Diane: Open voicings, different chords each bar
# Bar 2: Fm7 (F, Ab, C, D)
piano_notes = [
    pretty_midi.Note(velocity=95, pitch=71, start=1.5, end=3.0), # F4
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=3.0), # Ab4
    pretty_midi.Note(velocity=85, pitch=72, start=1.5, end=3.0), # C5
    pretty_midi.Note(velocity=80, pitch=74, start=1.5, end=3.0), # D5
]
piano.notes.extend(piano_notes)

# Dante: Motif - F, Ab, C, Bb
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=81, start=1.5, end=1.625), # F5
    pretty_midi.Note(velocity=100, pitch=78, start=1.625, end=1.75), # Ab5
    pretty_midi.Note(velocity=100, pitch=82, start=1.75, end=1.875), # C6
    pretty_midi.Note(velocity=100, pitch=79, start=1.875, end=2.0), # Bb5
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Marcus: Walking bass line in Fm
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=53, start=3.0, end=3.375), # F2
    pretty_midi.Note(velocity=90, pitch=50, start=3.375, end=3.75), # Ab2
    pretty_midi.Note(velocity=90, pitch=51, start=3.75, end=4.125), # D2
    pretty_midi.Note(velocity=90, pitch=53, start=4.125, end=4.5), # F2
]
bass.notes.extend(bass_notes)

# Diane: Open voicings, different chords each bar
# Bar 3: Bb7 (Bb, D, F, Ab)
piano_notes = [
    pretty_midi.Note(velocity=95, pitch=70, start=3.0, end=4.5), # Bb4
    pretty_midi.Note(velocity=90, pitch=74, start=3.0, end=4.5), # D5
    pretty_midi.Note(velocity=85, pitch=71, start=3.0, end=4.5), # F5
    pretty_midi.Note(velocity=80, pitch=67, start=3.0, end=4.5), # Ab4
]
piano.notes.extend(piano_notes)

# Dante: Motif - F, Ab, C, Bb (repeat with variation)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=81, start=3.0, end=3.125), # F5
    pretty_midi.Note(velocity=100, pitch=78, start=3.125, end=3.25), # Ab5
    pretty_midi.Note(velocity=100, pitch=82, start=3.25, end=3.375), # C6
    pretty_midi.Note(velocity=100, pitch=79, start=3.375, end=3.5), # Bb5
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Marcus: Walking bass line in Fm
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=53, start=4.5, end=4.875), # F2
    pretty_midi.Note(velocity=90, pitch=50, start=4.875, end=5.25), # Ab2
    pretty_midi.Note(velocity=90, pitch=51, start=5.25, end=5.625), # D2
    pretty_midi.Note(velocity=90, pitch=53, start=5.625, end=6.0), # F2
]
bass.notes.extend(bass_notes)

# Diane: Open voicings, different chords each bar
# Bar 4: D7 (D, F#, A, C)
piano_notes = [
    pretty_midi.Note(velocity=95, pitch=74, start=4.5, end=6.0), # D5
    pretty_midi.Note(velocity=90, pitch=76, start=4.5, end=6.0), # F#5
    pretty_midi.Note(velocity=85, pitch=77, start=4.5, end=6.0), # A5
    pretty_midi.Note(velocity=80, pitch=71, start=4.5, end=6.0), # C5
]
piano.notes.extend(piano_notes)

# Dante: Motif - F, Ab, C, Bb (return and finish)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=81, start=4.5, end=4.625), # F5
    pretty_midi.Note(velocity=100, pitch=78, start=4.625, end=4.75), # Ab5
    pretty_midi.Note(velocity=100, pitch=82, start=4.75, end=4.875), # C6
    pretty_midi.Note(velocity=100, pitch=79, start=4.875, end=5.0), # Bb5
]
sax.notes.extend(sax_notes)

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("intro_wayne.mid")
