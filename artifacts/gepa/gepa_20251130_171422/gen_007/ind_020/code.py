
import pretty_midi

# Create MIDI file with 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Double Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drums: kick=36, snare=38, hihat=42
drum_kick = 36
drum_snare = 38
drum_hihat = 42

# Set up the time signature (4/4)
midi.time_signature_changes = [pretty_midi.TimeSignature(numerator=4, denominator=4, time=0)]

# BAR 1: DRUMS ALONE — build tension with hihat & kick
drum_kick_note = pretty_midi.Note(velocity=100, pitch=drum_kick, start=0.0, end=0.375)
drum_kick_note2 = pretty_midi.Note(velocity=100, pitch=drum_kick, start=1.125, end=1.5)
drum_kick_note3 = pretty_midi.Note(velocity=100, pitch=drum_kick, start=2.25, end=2.625)
drum_kick_note4 = pretty_midi.Note(velocity=100, pitch=drum_kick, start=3.375, end=3.75)

drum_snare_note = pretty_midi.Note(velocity=110, pitch=drum_snare, start=0.75, end=1.125)
drum_snare_note2 = pretty_midi.Note(velocity=110, pitch=drum_snare, start=1.875, end=2.25)
drum_snare_note3 = pretty_midi.Note(velocity=110, pitch=drum_snare, start=3.0, end=3.375)

drum_hihat_notes = []
for i in range(0, 6):
    start = i * 0.375
    end = start + 0.375
    drum_hihat_notes.append(pretty_midi.Note(velocity=90, pitch=drum_hihat, start=start, end=end))

drums.notes.extend([drum_kick_note, drum_kick_note2, drum_kick_note3, drum_kick_note4,
                    drum_snare_note, drum_snare_note2, drum_snare_note3] + drum_hihat_notes)

# BAR 2: BASS + PIANO — enter with the key center (Dm7)
# Bass: walking line with chromatic motion
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=60, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=2.625, end=3.0),  # E
]

# Piano: comp on 2 and 4 with 7th chords
piano_notes = [
    # Bar 2, beat 2: Dm7
    pretty_midi.Note(velocity=100, pitch=62, start=1.875, end=2.25),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=1.875, end=2.25),  # C

    # Bar 2, beat 4: G7
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # B
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.375),  # C
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.375),  # D
]

bass.notes.extend(bass_notes)
piano.notes.extend(piano_notes)

# BAR 3: SAX + DRUMS — the motif begins
# Sax: a simple but striking motif — D (62), F (65), D (62), F# (66)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=110, pitch=65, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=110, pitch=62, start=3.75, end=4.125),  # D
    pretty_midi.Note(velocity=110, pitch=66, start=4.125, end=4.5),  # F#
]

# Add the same drums to Bar 3 as in Bar 1
for note in drums.notes:
    if note.start >= 1.5 and note.start < 3.0:
        new_note = pretty_midi.Note(
            velocity=note.velocity,
            pitch=note.pitch,
            start=note.start + 1.5,
            end=note.end + 1.5
        )
        drums.notes.append(new_note)

sax.notes.extend(sax_notes)

# BAR 4: BASS + PIANO + SAX — motif resolution
# Bass: follow the melody D-F-D-F#
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=90, pitch=65, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=90, pitch=62, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=90, pitch=66, start=5.625, end=6.0),  # F#

    # End with a chromatic lead into the next phrase
    pretty_midi.Note(velocity=90, pitch=67, start=5.625, end=5.75),
    pretty_midi.Note(velocity=90, pitch=68, start=5.75, end=5.875),
    pretty_midi.Note(velocity=90, pitch=69, start=5.875, end=6.0),
]

# Piano: comp with Dm7 again
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.875),  # C

    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=72, start=5.25, end=5.625),
]

# Sax: repeat the motif, but end on a sustained note
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=110, pitch=65, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=110, pitch=62, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=110, pitch=66, start=5.625, end=6.0),  # F#
]

bass.notes.extend(bass_notes)
piano.notes.extend(piano_notes)
sax.notes.extend(sax_notes)

# Add all instruments to the MIDI
midi.instruments.append(sax)
midi.instruments.append(bass)
midi.instruments.append(piano)
midi.instruments.append(drums)

# Save the MIDI
midi.write("dante_intro.mid")
