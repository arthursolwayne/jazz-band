
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
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # D2 (MIDI 38) on beat 1
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),
    # Chromatic approach to G2 (MIDI 43) on & of 1
    pretty_midi.Note(velocity=70, pitch=42, start=1.875, end=2.0),
    # G2 (MIDI 43) on beat 2
    pretty_midi.Note(velocity=90, pitch=43, start=2.0, end=2.375),
    # Chromatic approach to A2 (MIDI 45) on & of 2
    pretty_midi.Note(velocity=70, pitch=44, start=2.375, end=2.5625),
    # A2 (MIDI 45) on beat 3
    pretty_midi.Note(velocity=90, pitch=45, start=2.5625, end=2.9375),
    # Chromatic approach to D3 (MIDI 50) on & of 3
    pretty_midi.Note(velocity=70, pitch=49, start=2.9375, end=3.125),
    # D3 (MIDI 50) on beat 4
    pretty_midi.Note(velocity=90, pitch=50, start=3.125, end=3.5),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dmaj7 (D-F#-A-C#)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=3.0),  # D4
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=3.0),  # F#4
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=3.0),  # A4
    pretty_midi.Note(velocity=90, pitch=76, start=1.5, end=3.0),  # C#5
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Start with a D4 (MIDI 62) on beat 1
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),
    # Move to F#4 (MIDI 67) on & of 1
    pretty_midi.Note(velocity=110, pitch=67, start=1.875, end=2.0),
    # Leave it hanging on A4 (MIDI 71) on beat 2
    pretty_midi.Note(velocity=110, pitch=71, start=2.0, end=2.375),
    # Come back and finish with D5 (MIDI 72) on beat 3
    pretty_midi.Note(velocity=110, pitch=72, start=2.5625, end=2.9375),
    # End on C#5 (MIDI 76) on beat 4
    pretty_midi.Note(velocity=110, pitch=76, start=3.125, end=3.5),
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # G2 (MIDI 43) on beat 1
    pretty_midi.Note(velocity=90, pitch=43, start=3.0, end=3.375),
    # Chromatic approach to A2 (MIDI 45) on & of 1
    pretty_midi.Note(velocity=70, pitch=44, start=3.375, end=3.5625),
    # A2 (MIDI 45) on beat 2
    pretty_midi.Note(velocity=90, pitch=45, start=3.5625, end=3.9375),
    # Chromatic approach to B2 (MIDI 47) on & of 2
    pretty_midi.Note(velocity=70, pitch=46, start=3.9375, end=4.125),
    # B2 (MIDI 47) on beat 3
    pretty_midi.Note(velocity=90, pitch=47, start=4.125, end=4.5),
    # Chromatic approach to D3 (MIDI 50) on & of 3
    pretty_midi.Note(velocity=70, pitch=49, start=4.5, end=4.6875),
    # D3 (MIDI 50) on beat 4
    pretty_midi.Note(velocity=90, pitch=50, start=4.6875, end=5.0),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 3: Gmaj7 (G-B-D-F#)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.5),  # G4
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=4.5),  # B4
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=4.5),  # D5
    pretty_midi.Note(velocity=90, pitch=78, start=3.0, end=4.5),  # F#5
]
piano.notes.extend(piano_notes)

# Sax: Continue the motif, develop it
sax_notes = [
    # Continue from D5 (MIDI 72) on beat 1
    pretty_midi.Note(velocity=110, pitch=72, start=3.0, end=3.375),
    # Move to F#5 (MIDI 78) on & of 1
    pretty_midi.Note(velocity=110, pitch=78, start=3.375, end=3.5625),
    # Leave it hanging on B5 (MIDI 81) on beat 2
    pretty_midi.Note(velocity=110, pitch=81, start=3.5625, end=3.9375),
    # Come back and finish with G5 (MIDI 79) on beat 3
    pretty_midi.Note(velocity=110, pitch=79, start=4.125, end=4.5),
    # End on D6 (MIDI 82) on beat 4
    pretty_midi.Note(velocity=110, pitch=82, start=4.6875, end=5.0),
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # D3 (MIDI 50) on beat 1
    pretty_midi.Note(velocity=90, pitch=50, start=4.5, end=4.875),
    # Chromatic approach to E3 (MIDI 52) on & of 1
    pretty_midi.Note(velocity=70, pitch=51, start=4.875, end=5.0625),
    # E3 (MIDI 52) on beat 2
    pretty_midi.Note(velocity=90, pitch=52, start=5.0625, end=5.4375),
    # Chromatic approach to F#3 (MIDI 54) on & of 2
    pretty_midi.Note(velocity=70, pitch=53, start=5.4375, end=5.625),
    # F#3 (MIDI 54) on beat 3
    pretty_midi.Note(velocity=90, pitch=54, start=5.625, end=6.0),
    # Chromatic approach to G3 (MIDI 55) on & of 3
    pretty_midi.Note(velocity=70, pitch=54, start=5.625, end=5.8125),
    # G3 (MIDI 55) on beat 4
    pretty_midi.Note(velocity=90, pitch=55, start=5.8125, end=6.0),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 4: Amaj7 (A-C#-E-G#)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=6.0),  # A4
    pretty_midi.Note(velocity=90, pitch=76, start=4.5, end=6.0),  # C#5
    pretty_midi.Note(velocity=100, pitch=79, start=4.5, end=6.0),  # E5
    pretty_midi.Note(velocity=90, pitch=83, start=4.5, end=6.0),  # G#5
]
piano.notes.extend(piano_notes)

# Sax: Finish the motif, resolve it
sax_notes = [
    # Continue from G5 (MIDI 79) on beat 1
    pretty_midi.Note(velocity=110, pitch=79, start=4.5, end=4.875),
    # Move to A5 (MIDI 81) on & of 1
    pretty_midi.Note(velocity=110, pitch=81, start=4.875, end=5.0625),
    # Leave it hanging on C#6 (MIDI 84) on beat 2
    pretty_midi.Note(velocity=110, pitch=84, start=5.0625, end=5.4375),
    # Come back and finish with D6 (MIDI 82) on beat 3
    pretty_midi.Note(velocity=110, pitch=82, start=5.625, end=6.0),
]
sax.notes.extend(sax_notes)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=5.8125),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=5.0625, end=5.1875),
    pretty_midi.Note(velocity=110, pitch=38, start=5.8125, end=6.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.0625, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=5.4375, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=5.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=5.8125, end=6.0),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
