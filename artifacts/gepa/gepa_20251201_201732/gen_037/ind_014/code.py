
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante - Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Marcus - Double Bass
piano = pretty_midi.Instrument(program=0)      # Diane - Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray - Drums

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here — a tight, energetic groove with space
drum_notes = [
    # Bar 1: Kick on 1 & 3, snare on 2 & 4, hihat on every 8th
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),  # Snare on 4
    # Hi-hats on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Time signature: 4/4, 160 BPM => 0.375s per beat

## Drums
bar2_drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875), # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),  # Snare on 4
    # Hi-hats on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
]
drums.notes.extend(bar2_drum_notes)

## Bass (Marcus) - Walking line in D
# D2 (MIDI 38) to G2 (MIDI 43), roots and fifths with chromatic approaches
# Bar 2: D2 - C#2 - D2 - F#2 (D, chromatic down, D, fifths up)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875), # D2 (Root)
    pretty_midi.Note(velocity=80, pitch=37, start=1.875, end=2.25), # C#2 (chromatic down)
    pretty_midi.Note(velocity=80, pitch=38, start=2.25, end=2.625), # D2 (Root again)
    pretty_midi.Note(velocity=80, pitch=41, start=2.625, end=3.0),  # F#2 (fifth)
]
bass.notes.extend(bass_notes)

## Piano (Diane) - Open voicings, different chord each bar
# Bar 2: D7sus4 (D, G, A) — open voicing, resolve on 4th beat
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=3.0),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=3.0),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=3.0),  # A4
]
piano.notes.extend(piano_notes)

## Sax (Dante) - One short motif, make it sing
# D4 - F#4 (up a minor third), then let it hang
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875), # D4
    pretty_midi.Note(velocity=110, pitch=66, start=1.875, end=2.25), # F#4
    pretty_midi.Note(velocity=110, pitch=62, start=2.25, end=2.625), # D4 (rest)
    pretty_midi.Note(velocity=110, pitch=62, start=2.625, end=3.0),  # D4 (rest)
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
## Drums
bar3_drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375), # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),  # Snare on 4
    # Hi-hats on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
]
drums.notes.extend(bar3_drum_notes)

## Bass (Marcus) - D2 - E2 - F#2 - G2 (chromatic up)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=3.0, end=3.375), # D2
    pretty_midi.Note(velocity=80, pitch=39, start=3.375, end=3.75), # E2
    pretty_midi.Note(velocity=80, pitch=40, start=3.75, end=4.125), # F#2
    pretty_midi.Note(velocity=80, pitch=41, start=4.125, end=4.5),  # G2
]
bass.notes.extend(bass_notes)

## Piano (Diane) - Open voicings, different chord each bar
# Bar 3: G7sus4 (G, B, D) — open voicing, resolve on 4th beat
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.5),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=4.5),  # B4
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=4.5),  # D5
]
piano.notes.extend(piano_notes)

## Sax (Dante) - Continue the motif — repeat it, but leave it open
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.375), # D4
    pretty_midi.Note(velocity=110, pitch=66, start=3.375, end=3.75), # F#4
    pretty_midi.Note(velocity=110, pitch=62, start=3.75, end=4.125), # D4 (rest)
    pretty_midi.Note(velocity=110, pitch=62, start=4.125, end=4.5),  # D4 (rest)
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
## Drums
bar4_drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875), # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),  # Snare on 4
    # Hi-hats on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
]
drums.notes.extend(bar4_drum_notes)

## Bass (Marcus) - G2 - A2 - B2 - C#3 (chromatic up)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=41, start=4.5, end=4.875), # G2
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25), # A2
    pretty_midi.Note(velocity=80, pitch=43, start=5.25, end=5.625), # B2
    pretty_midi.Note(velocity=80, pitch=45, start=5.625, end=6.0),  # C#3
]
bass.notes.extend(bass_notes)

## Piano (Diane) - Open voicings, different chord each bar
# Bar 4: B7sus4 (B, D#, F#) — open voicing, resolve on 4th beat
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=6.0),  # B4
    pretty_midi.Note(velocity=100, pitch=75, start=4.5, end=6.0),  # D#5
    pretty_midi.Note(velocity=100, pitch=73, start=4.5, end=6.0),  # F#5
]
piano.notes.extend(piano_notes)

## Sax (Dante) - Final statement of the motif — complete it
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.875), # D4
    pretty_midi.Note(velocity=110, pitch=66, start=4.875, end=5.25), # F#4
    pretty_midi.Note(velocity=110, pitch=67, start=5.25, end=5.625), # G4 (resolution)
    pretty_midi.Note(velocity=110, pitch=62, start=5.625, end=6.0),  # D4 (rest)
]
sax.notes.extend(sax_notes)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
