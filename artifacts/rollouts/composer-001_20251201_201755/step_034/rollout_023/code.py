
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
# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # D2 (38) on 1
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),
    # Eb2 (39) approach to G2 (43)
    pretty_midi.Note(velocity=90, pitch=39, start=1.875, end=2.0),
    # G2 (43) on 2
    pretty_midi.Note(velocity=100, pitch=43, start=2.0, end=2.375),
    # A2 (45) approach to D3 (50)
    pretty_midi.Note(velocity=90, pitch=45, start=2.375, end=2.5),
    # D3 (50) on 3
    pretty_midi.Note(velocity=100, pitch=50, start=2.5, end=2.875),
    # Eb3 (51) approach to G3 (55)
    pretty_midi.Note(velocity=90, pitch=51, start=2.875, end=3.0),
    # G3 (55) on 4
    pretty_midi.Note(velocity=100, pitch=55, start=3.0, end=3.375)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dmaj7 (D-F#-A-C#)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=3.0),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=3.0),  # F#4
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=3.0),  # A4
    pretty_midi.Note(velocity=100, pitch=73, start=1.5, end=3.0),  # C#4
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Start with a triplet on D4 (62)
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.625),
    pretty_midi.Note(velocity=110, pitch=62, start=1.625, end=1.75),
    pretty_midi.Note(velocity=110, pitch=62, start=1.75, end=1.875),
    # Leave it hanging with a grace note on E4 (64)
    pretty_midi.Note(velocity=70, pitch=64, start=1.875, end=1.9375),
    # Come back with a descending line to B3 (61)
    pretty_midi.Note(velocity=110, pitch=61, start=2.0, end=2.125),
    pretty_midi.Note(velocity=110, pitch=59, start=2.125, end=2.25),
    pretty_midi.Note(velocity=110, pitch=57, start=2.25, end=2.375),
    pretty_midi.Note(velocity=110, pitch=55, start=2.375, end=2.5)
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # D3 (50) on 1
    pretty_midi.Note(velocity=100, pitch=50, start=3.0, end=3.375),
    # Eb3 (51) approach to G3 (55)
    pretty_midi.Note(velocity=90, pitch=51, start=3.375, end=3.5),
    # G3 (55) on 2
    pretty_midi.Note(velocity=100, pitch=55, start=3.5, end=3.875),
    # A3 (57) approach to D4 (62)
    pretty_midi.Note(velocity=90, pitch=57, start=3.875, end=4.0),
    # D4 (62) on 3
    pretty_midi.Note(velocity=100, pitch=62, start=4.0, end=4.375),
    # Eb4 (63) approach to G4 (67)
    pretty_midi.Note(velocity=90, pitch=63, start=4.375, end=4.5),
    # G4 (67) on 4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 3: G7 (G-B-D-F)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.5),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=4.5),  # B4
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=4.5),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=4.5),  # F4
]
piano.notes.extend(piano_notes)

# Sax: Continue the motif, resolve with a descending line
sax_notes = [
    # Continue descending line to F#3 (60)
    pretty_midi.Note(velocity=110, pitch=60, start=3.0, end=3.125),
    pretty_midi.Note(velocity=110, pitch=58, start=3.125, end=3.25),
    pretty_midi.Note(velocity=110, pitch=55, start=3.25, end=3.375),
    # End with a small trill on G3 (61)
    pretty_midi.Note(velocity=110, pitch=61, start=3.375, end=3.4375),
    pretty_midi.Note(velocity=110, pitch=61, start=3.4375, end=3.5)
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # G4 (67) on 1
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),
    # Ab4 (68) approach to B4 (71)
    pretty_midi.Note(velocity=90, pitch=68, start=4.875, end=5.0),
    # B4 (71) on 2
    pretty_midi.Note(velocity=100, pitch=71, start=5.0, end=5.375),
    # C#4 (73) approach to D4 (62)
    pretty_midi.Note(velocity=90, pitch=73, start=5.375, end=5.5),
    # D4 (62) on 3
    pretty_midi.Note(velocity=100, pitch=62, start=5.5, end=5.875),
    # Eb4 (63) approach to G4 (67)
    pretty_midi.Note(velocity=90, pitch=63, start=5.875, end=6.0),
    # G4 (67) on 4
    pretty_midi.Note(velocity=100, pitch=67, start=6.0, end=6.375)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 4: Dmaj7 (D-F#-A-C#)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=6.0),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=6.0),  # F#4
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=6.0),  # A4
    pretty_midi.Note(velocity=100, pitch=73, start=4.5, end=6.0),  # C#4
]
piano.notes.extend(piano_notes)

# Sax: Final resolution with a trill on D4 (62)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.5625),
    pretty_midi.Note(velocity=110, pitch=62, start=4.5625, end=4.625),
    pretty_midi.Note(velocity=110, pitch=62, start=4.625, end=4.6875),
    pretty_midi.Note(velocity=110, pitch=62, start=4.6875, end=4.75),
    pretty_midi.Note(velocity=110, pitch=62, start=4.75, end=4.8125),
    pretty_midi.Note(velocity=110, pitch=62, start=4.8125, end=4.875)
]
sax.notes.extend(sax_notes)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.375),
    pretty_midi.Note(velocity=110, pitch=38, start=6.375, end=6.5),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.0625, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=5.4375, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=5.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=5.8125, end=6.0)
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Write the MIDI file
# midi.write disabled
