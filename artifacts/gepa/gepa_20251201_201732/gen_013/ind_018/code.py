
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: walking line starting at D2 (MIDI 38) with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875), # D2
    pretty_midi.Note(velocity=100, pitch=40, start=1.875, end=2.25), # F2
    pretty_midi.Note(velocity=100, pitch=39, start=2.25, end=2.625), # Eb2
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0), # G2
    pretty_midi.Note(velocity=100, pitch=43, start=3.0, end=3.375), # G#2
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75), # G2
    pretty_midi.Note(velocity=100, pitch=40, start=3.75, end=4.125), # F2
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5), # D2
    pretty_midi.Note(velocity=100, pitch=40, start=4.5, end=4.875), # F2
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25), # G2
    pretty_midi.Note(velocity=100, pitch=43, start=5.25, end=5.625), # G#2
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0), # G2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: D7 (C#4, D4, F#4, A4)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=63, start=1.5, end=2.25), # C#4
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=2.25), # D4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=2.25), # F#4
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=2.25), # A4
]

# Bar 3: G7 (F#4, G4, B4, D5)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=3.0), # F#4
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=3.0), # G4
    pretty_midi.Note(velocity=100, pitch=76, start=2.25, end=3.0), # B4
    pretty_midi.Note(velocity=100, pitch=79, start=2.25, end=3.0), # D5
])

# Bar 4: Cmaj7 (B3, C4, E4, G4)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=61, start=3.0, end=3.75), # B3
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.75), # C4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.75), # E4
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.75), # G4
])

# Bar 4 continued: resolution chord (D7)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=63, start=3.75, end=4.5), # C#4
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.5), # D4
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.5), # F#4
    pretty_midi.Note(velocity=100, pitch=71, start=3.75, end=4.5), # A4
])

piano.notes.extend(piano_notes)

# Sax: Motif - short, singable, leaves it hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875), # D4
    pretty_midi.Note(velocity=100, pitch=66, start=1.875, end=2.25), # E4
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.625), # D4
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0), # C4
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375), # D4
    pretty_midi.Note(velocity=100, pitch=66, start=3.375, end=3.75), # E4
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.125), # D4
    pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.5), # C4
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875), # D4
    pretty_midi.Note(velocity=100, pitch=66, start=4.875, end=5.25), # E4
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.625), # D4
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=6.0), # C4
]
sax.notes.extend(sax_notes)

# Drums: Bars 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    # Kick on 1 (start)
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375))
    # Snare on 2 (start + 0.75)
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125))
    # Kick on 3 (start + 1.125)
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5))
    # Snare on 4 (start + 1.5)
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 1.5, end=start + 1.875))
    # Hihat on every eighth
    for i in range(0, 4):
        drum_notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start + i * 0.375, end=start + (i + 1) * 0.375))

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_russo_4bar.mid")
