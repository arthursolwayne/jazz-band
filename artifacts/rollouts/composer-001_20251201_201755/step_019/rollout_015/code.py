
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
drum_notes = []
for beat in range(4):
    if beat % 2 == 0:
        drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=beat * 0.375, end=(beat + 1) * 0.375))
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=beat * 0.375, end=(beat + 1) * 0.375))
    drum_notes.append(pretty_midi.Note(velocity=80, pitch=42, start=beat * 0.375, end=(beat + 1) * 0.375))
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=80, pitch=41, start=1.875, end=2.25), # F#2
    pretty_midi.Note(velocity=80, pitch=43, start=2.25, end=2.625), # A2
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),  # G2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2: Fmaj7 (F, A, C, E)
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=3.0),  # F (MIDI 71)
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=3.0),  # A
    pretty_midi.Note(velocity=100, pitch=79, start=1.5, end=3.0),  # C
    pretty_midi.Note(velocity=100, pitch=82, start=1.5, end=3.0),  # E
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # A (Fmaj7 3rd)
    pretty_midi.Note(velocity=100, pitch=71, start=1.875, end=2.25),  # B (Fmaj7 5th)
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # E (Fmaj7 7th)
    pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=3.0),   # A (Fmaj7 3rd)
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),  # G2
    pretty_midi.Note(velocity=80, pitch=44, start=3.375, end=3.75), # Bb2
    pretty_midi.Note(velocity=80, pitch=43, start=3.75, end=4.125), # A2
    pretty_midi.Note(velocity=80, pitch=41, start=4.125, end=4.5),  # F#2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 3: Bbmaj7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.5),  # Bb (MIDI 67)
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=4.5),  # D
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=4.5),  # F
    pretty_midi.Note(velocity=100, pitch=77, start=3.0, end=4.5),  # Ab
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # Bb (Bbmaj7 3rd)
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.75),  # B (Bbmaj7 5th)
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.125),  # E (Bbmaj7 7th)
    pretty_midi.Note(velocity=100, pitch=67, start=4.125, end=4.5),   # Bb (Bbmaj7 3rd)
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=41, start=4.5, end=4.875),  # F#2
    pretty_midi.Note(velocity=80, pitch=43, start=4.875, end=5.25), # A2
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625), # G2
    pretty_midi.Note(velocity=80, pitch=38, start=5.625, end=6.0),  # D2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 4: Fmaj7 (F, A, C, E)
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=6.0),  # F (MIDI 71)
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=6.0),  # A
    pretty_midi.Note(velocity=100, pitch=79, start=4.5, end=6.0),  # C
    pretty_midi.Note(velocity=100, pitch=82, start=4.5, end=6.0),  # E
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),  # A (Fmaj7 3rd)
    pretty_midi.Note(velocity=100, pitch=71, start=4.875, end=5.25),  # B (Fmaj7 5th)
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625),  # E (Fmaj7 7th)
    pretty_midi.Note(velocity=100, pitch=69, start=5.625, end=6.0),   # A (Fmaj7 3rd)
]
sax.notes.extend(sax_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = []
for beat in range(4):
    if beat % 2 == 0:
        drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=(beat + 2) * 0.375, end=(beat + 3) * 0.375))
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=(beat + 2) * 0.375, end=(beat + 3) * 0.375))
    drum_notes.append(pretty_midi.Note(velocity=80, pitch=42, start=(beat + 2) * 0.375, end=(beat + 3) * 0.375))
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
