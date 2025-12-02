
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
    # Hihat on every eighth
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

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line, chromatic approaches, never the same note twice. He's the anchor.
bass_notes = [
    # Bar 2: D - C# - D - E
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875), # D
    pretty_midi.Note(velocity=90, pitch=61, start=1.875, end=2.25), # C#
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.625), # D
    pretty_midi.Note(velocity=90, pitch=64, start=2.625, end=3.0), # E
    # Bar 3: F - E - F - G
    pretty_midi.Note(velocity=90, pitch=65, start=3.0, end=3.375), # F
    pretty_midi.Note(velocity=90, pitch=64, start=3.375, end=3.75), # E
    pretty_midi.Note(velocity=90, pitch=65, start=3.75, end=4.125), # F
    pretty_midi.Note(velocity=90, pitch=67, start=4.125, end=4.5), # G
    # Bar 4: A - G - A - B
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.875), # A
    pretty_midi.Note(velocity=90, pitch=67, start=4.875, end=5.25), # G
    pretty_midi.Note(velocity=90, pitch=69, start=5.25, end=5.625), # A
    pretty_midi.Note(velocity=90, pitch=71, start=5.625, end=6.0), # B
]
bass.notes.extend(bass_notes)

# Diane: 7th chords, comp on 2 and 4. Stay out of your way but keep it moving.
piano_notes = [
    # Bar 2: D7 on 2 and 4
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625), # D
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.625), # A
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625), # C#
    pretty_midi.Note(velocity=100, pitch=74, start=2.25, end=2.625), # D
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125), # D
    pretty_midi.Note(velocity=100, pitch=72, start=3.75, end=4.125), # A
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.125), # C#
    pretty_midi.Note(velocity=100, pitch=74, start=3.75, end=4.125), # D
    # Bar 3: G7 on 2 and 4
    pretty_midi.Note(velocity=100, pitch=71, start=4.125, end=4.5), # G
    pretty_midi.Note(velocity=100, pitch=76, start=4.125, end=4.5), # D
    pretty_midi.Note(velocity=100, pitch=74, start=4.125, end=4.5), # B
    pretty_midi.Note(velocity=100, pitch=78, start=4.125, end=4.5), # F#
    pretty_midi.Note(velocity=100, pitch=71, start=5.625, end=6.0), # G
    pretty_midi.Note(velocity=100, pitch=76, start=5.625, end=6.0), # D
    pretty_midi.Note(velocity=100, pitch=74, start=5.625, end=6.0), # B
    pretty_midi.Note(velocity=100, pitch=78, start=5.625, end=6.0), # F#
]
piano.notes.extend(piano_notes)

# You: This is your moment. One short motif, make it sing. Start it, leave it hanging. Come back and finish it. No scale runs — that's student shit.
sax_notes = [
    # Bar 2: Start the motif
    pretty_midi.Note(velocity=110, pitch=69, start=1.5, end=1.6875), # A
    pretty_midi.Note(velocity=110, pitch=71, start=1.6875, end=1.875), # B
    pretty_midi.Note(velocity=110, pitch=72, start=1.875, end=2.0), # C
    # Bar 3: Leave it hanging
    pretty_midi.Note(velocity=110, pitch=69, start=3.0, end=3.1875), # A
    pretty_midi.Note(velocity=110, pitch=71, start=3.1875, end=3.375), # B
    # Bar 4: Come back and finish it
    pretty_midi.Note(velocity=110, pitch=72, start=5.25, end=5.4375), # C
    pretty_midi.Note(velocity=110, pitch=71, start=5.4375, end=5.625), # B
    pretty_midi.Note(velocity=110, pitch=69, start=5.625, end=5.8125), # A
    pretty_midi.Note(velocity=110, pitch=67, start=5.8125, end=6.0), # G
]
sax.notes.extend(sax_notes)

# Drums: Bar 2-4
# Kicks on 1 and 3
for bar in range(2, 4):
    start = bar * 1.5
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    drums.notes.append(kick1)
    drums.notes.append(kick2)
# Snares on 2 and 4
for bar in range(2, 4):
    start = bar * 1.5
    snare1 = pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 0.875)
    snare2 = pretty_midi.Note(velocity=110, pitch=38, start=start + 1.875, end=start + 2.0)
    drums.notes.append(snare1)
    drums.notes.append(snare2)
# Hihats on every eighth
for bar in range(2, 4):
    start = bar * 1.5
    for i in range(8):
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.1875, end=start + (i + 1) * 0.1875)
        drums.notes.append(hihat)

midi.instruments.extend([sax, bass, piano, drums])

# Save to MIDI file
midi.write("dante_intro.mid")
