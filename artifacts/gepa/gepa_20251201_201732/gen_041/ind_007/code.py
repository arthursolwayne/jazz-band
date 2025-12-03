
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
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Bar 2 (1.5 - 3.0s)
# Marcus: Walking bass line, D2-G2 (MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # D2 (MIDI 38)
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),
    # F#2 (MIDI 41) chromatic approach
    pretty_midi.Note(velocity=90, pitch=41, start=1.875, end=2.125),
    # G2 (MIDI 43)
    pretty_midi.Note(velocity=90, pitch=43, start=2.125, end=2.5),
    # F#2 (MIDI 41)
    pretty_midi.Note(velocity=90, pitch=41, start=2.5, end=2.875),
    # D2 (MIDI 38)
    pretty_midi.Note(velocity=90, pitch=38, start=2.875, end=3.0),
]

for note in bass_notes:
    bass.notes.append(note)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: D7 (G, D, F#, A)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=3.0), # G4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=3.0), # D4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=3.0), # F#4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=3.0), # A4
]

for note in piano_notes:
    piano.notes.append(note)

# Bar 3 (3.0 - 4.5s)
# Diane: Bm7 (D, F#, A, C#)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.5), # D4
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=4.5), # F#4
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=4.5), # A4
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=4.5), # C#4
]

for note in piano_notes:
    piano.notes.append(note)

# Bar 4 (4.5 - 6.0s)
# Diane: Gmaj7 (B, D, F#, G)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=6.0), # B4
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=6.0), # D4
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=6.0), # F#4
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=6.0), # G4
]

for note in piano_notes:
    piano.notes.append(note)

# Dante: Tenor sax, one short motif, start it, leave it hanging, come back and finish it
# Bar 2: E (MIDI 64) on beat 1
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=64, start=1.5, end=1.875),
    # Leave it hanging
    # Bar 3: A (MIDI 69) on beat 3
    pretty_midi.Note(velocity=110, pitch=69, start=3.375, end=3.75),
    # Bar 4: D (MIDI 67) on beat 1
    pretty_midi.Note(velocity=110, pitch=67, start=4.5, end=4.875),
    # Finish it with B (MIDI 67) on beat 3
    pretty_midi.Note(velocity=110, pitch=67, start=5.625, end=6.0),
]

for note in sax_notes:
    sax.notes.append(note)

# Add drum fill in bar 4
# Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.375),
    pretty_midi.Note(velocity=110, pitch=38, start=6.0, end=6.125),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=90, pitch=42, start=6.0, end=6.375),
    pretty_midi.Note(velocity=90, pitch=42, start=6.375, end=6.75),
    pretty_midi.Note(velocity=90, pitch=42, start=6.75, end=7.125),
    pretty_midi.Note(velocity=90, pitch=42, start=7.125, end=7.5),
]

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
