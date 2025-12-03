
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
#ONLY drums here. No piano, bass, or sax until bar 2.
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
    # D2 (MIDI 38) on 1
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),
    # F#2 (MIDI 41) on 2 (chromatic approach to G2)
    pretty_midi.Note(velocity=90, pitch=41, start=1.875, end=2.125),
    # G2 (MIDI 43) on 3
    pretty_midi.Note(velocity=90, pitch=43, start=2.125, end=2.5),
    # B2 (MIDI 46) on 4 (chromatic approach to C#3)
    pretty_midi.Note(velocity=90, pitch=46, start=2.5, end=2.75),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dmaj7 (D-F#-A-C#)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=3.0),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=3.0),  # F#4
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=3.0),  # A4
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=3.0),  # C#5
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Start with a D4 (MIDI 62) on beat 1
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),
    # Move to F#4 (MIDI 67) on beat 2
    pretty_midi.Note(velocity=110, pitch=67, start=1.875, end=2.125),
    # Leave it hanging on A4 (MIDI 71) on beat 3
    pretty_midi.Note(velocity=110, pitch=71, start=2.125, end=2.5),
    # Resolve on D5 (MIDI 67) on beat 4
    pretty_midi.Note(velocity=110, pitch=67, start=2.5, end=2.75),
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # C#3 (MIDI 48) on 1 (chromatic approach to D3)
    pretty_midi.Note(velocity=90, pitch=48, start=3.0, end=3.375),
    # D3 (MIDI 49) on 2
    pretty_midi.Note(velocity=90, pitch=49, start=3.375, end=3.625),
    # F#3 (MIDI 52) on 3 (chromatic approach to G3)
    pretty_midi.Note(velocity=90, pitch=52, start=3.625, end=4.0),
    # G3 (MIDI 53) on 4
    pretty_midi.Note(velocity=90, pitch=53, start=4.0, end=4.25),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 3: D7 (D-F#-A-C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=4.5),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.5),  # F#4
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=4.5),  # A4
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=4.5),  # C5
]
piano.notes.extend(piano_notes)

# Sax: Continue the motif, build tension
sax_notes = [
    # Continue from D5 (MIDI 67) on beat 1
    pretty_midi.Note(velocity=110, pitch=67, start=3.0, end=3.375),
    # Move to F#5 (MIDI 72) on beat 2
    pretty_midi.Note(velocity=110, pitch=72, start=3.375, end=3.625),
    # Leave it hanging on A5 (MIDI 76) on beat 3
    pretty_midi.Note(velocity=110, pitch=76, start=3.625, end=4.0),
    # Resolve on D6 (MIDI 74) on beat 4
    pretty_midi.Note(velocity=110, pitch=74, start=4.0, end=4.25),
]
sax.notes.extend(sax_notes)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.3125, end=4.5),
]
drums.notes.extend(drum_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # G3 (MIDI 53) on 1
    pretty_midi.Note(velocity=90, pitch=53, start=4.5, end=4.875),
    # A3 (MIDI 55) on 2 (chromatic approach to B3)
    pretty_midi.Note(velocity=90, pitch=55, start=4.875, end=5.125),
    # B3 (MIDI 57) on 3
    pretty_midi.Note(velocity=90, pitch=57, start=5.125, end=5.5),
    # D4 (MIDI 62) on 4 (chromatic approach to E4)
    pretty_midi.Note(velocity=90, pitch=62, start=5.5, end=5.75),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 4: Dm7 (D-F-A-C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=6.0),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=6.0),  # F4
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=6.0),  # A4
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=6.0),  # C5
]
piano.notes.extend(piano_notes)

# Sax: Finish the motif, resolve with a strong note
sax_notes = [
    # Continue from D6 (MIDI 74) on beat 1
    pretty_midi.Note(velocity=110, pitch=74, start=4.5, end=4.875),
    # Move to F6 (MIDI 77) on beat 2
    pretty_midi.Note(velocity=110, pitch=77, start=4.875, end=5.125),
    # Leave it hanging on A6 (MIDI 81) on beat 3
    pretty_midi.Note(velocity=110, pitch=81, start=5.125, end=5.5),
    # Resolve on D7 (MIDI 80) on beat 4
    pretty_midi.Note(velocity=110, pitch=80, start=5.5, end=5.75),
]
sax.notes.extend(sax_notes)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.375),
    pretty_midi.Note(velocity=110, pitch=38, start=6.25, end=6.5),
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
# midi.write disabled
